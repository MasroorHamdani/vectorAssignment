import logging
import logstash
import sys

class LogstashService():

    def __init__(self):
        self.host = 'localhost'
        self.logger = logging.getLogger('python-logstash-logger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logstash.LogstashHandler(self.host, 5959, version=1))
        # self.logger.addHandler(logstash.TCPLogstashHandler(host, 8345, version=1))

    def log(self, type, message, extra={}):
        if type == 'error':
            self.logger.error(message, extra=extra)
        elif type == 'warning':
            self.logger.warning(message, extra=extra)
        else:
            self.logger.info(message, extra=extra)


    
    
