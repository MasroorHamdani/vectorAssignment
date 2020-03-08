# vectorAssignment
=======

##Steps to Setup Local Environment.

###To clone the repository 
1. git clone https://github.com/MasroorHamdani/vectorAssignment.git

###To setup local environment dependencies
1. Install python3.
2. See if it works and show version as 3.x.x
   python3
3. Install Pip
   easy_install pip
4. Install python-virtualenv
   python3 -m pip install --user virtualenv
5. Create virtual environment.
   python3 -m virtualenv env
6. Activate it.
   source env/bin/activate
7. Install dependencies:
   pip3 install -r requirements.txt
8. Create DB
   python manage.py migrate
9. Create User
    python manage.py createsuperuser --email <email> --username <user>
    Add Password
10. Create new migration file -(If needed)
    python manage.py makemigrations
11. Verify tables created: login to DB
    python manage.py dbshell
    .tables

###To run the server
1. python3 manage.py runserver


# Part 1 - 
So far, from Part 1, I have defined the models and POST operation for country is defined. Also, some of the validations, like total population or total area defined in countries which belong to same continent, should be in range of population and area defined for the continent. Also continent name should be unique, that constraint is added from the DB side.

Next step, update and delete the Country table. Once that is done, same operation will be repeated for City table along with validations.
