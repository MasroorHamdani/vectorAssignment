from fabric import state
from fabric.api import task, run, local
import json
import os
import time


CAPTURE = False
NEVER_FAIL = False

COVERAGE_ENABLED = False
PROJECT_PACKGE = 'vectorassignment'


@task()
def docs_gen():
    '''Generates Documents. Picks sources from docs folder.'''
    local("sphinxbuilder")


@task()
def uml_gen():
    '''Generates Package Dependency Diagrams. Assumes Graphviz.'''
    local('bin/pyreverse -p deps %s' % PROJECT_PACKGE)
    local('mv *.dot out/')
    _ensure_dir('out/docs')
    local('dot -Tpng out/packages_deps.dot -o out/docs/packages_deps.png')


@task()
def runserver():
    '''Runs Django Server on port 8000'''
    local("python manage.py runserver 0.0.0.0:8000")


@task()
def lint_py():
    '''Reports PyLint Errors & Warnings for Python files'''
    return _execute('pylint --rcfile=etc/lint.rc --output-format={0} {1}'
                    .format("parseable", PROJECT_PACKGE))


@task()
def lint_js():
    '''Reports JSLint Errors & Warnings for JavaScript files'''
    return _execute('jshint --config=etc/jshint.json templates/')


@task()
def lint_css():
    '''Reports CSSLint Errors & Warnings for CSS files'''
    _execute('csslint --format junit-xml templates/static/css')  # TODO: Add option to specify csslint.json


@task()
def coverage():
    '''Enables Coverage. Used for test targets'''
    global COVERAGE_ENABLED
    COVERAGE_ENABLED = True


@task
def test(package=''):
    '''Run Tests for the given package fab test:<package>'''
    _ensure_dir('out/')
    result = None

    if COVERAGE_ENABLED:
        _execute("coverage erase --rcfile=.coveragerc")
        result = _execute("DJANGO_SETTINGS_MODULE=vectorassignment.test_settings coverage run --rcfile=.coveragerc manage.py test {}".format(PROJECT_PACKGE))
        _execute("coverage html --rcfile=.coveragerc")
        _execute("coverage xml --rcfile=.coveragerc")
    else:
        result = _execute('DJANGO_SETTINGS_MODULE=vectorassignment.test_settings python manage.py test {}'.format(PROJECT_PACKGE))

    return result


def _wait_for_completion(connection):
    deployments = connection.describe_deployments(STACK_ID)
    running = filter(lambda x: x['Status'] == 'running', deployments["Deployments"])

    if running:
        for run in running:
            print(run["Status"], "\t", run["Command"]["Name"], "\t", run["Comment"], "\t", run["Command"].get("Args"))
        time.sleep(5)
        _wait_for_completion(connection)


def _execute(cmd):
    if NEVER_FAIL:
        cmd = '%s; echo "Done"' % cmd

    return local(cmd, capture=CAPTURE)


def _ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
