mkdir djangotutorial

### start project

django-admin startproject mysite djangotutorial

### run project

python manage.py runserver

### create polls app

python manage.py startapp polls

### start migration

python manage.py migrate

### to see tables from SQLite CLI
sqlite3 db.sqlite3

.tables

.exit

### we need to tell our project that the polls app is installed
To include the app in our project; add a reference to its configuration class in the INSTALLED_APPS setting. The PollsConfig class is in the polls/apps.py file, so its dotted path is 'polls.apps.PollsConfig'. 

python manage.py makemigrations polls

#### The sqlmigrate command takes migration names and returns their SQL:
sqlmigrate command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required.

python manage.py sqlmigrate polls 0001

python manage.py check

this checks for any problems in your project without making migrations or touching the database.

run migrate again to create those model tables in your database (question & choice)

### three-step guide to making model changes:

1. Change your models (in models.py).

2. Run python manage.py makemigrations to create migrations for those changes

3. Run python manage.py migrate to apply those changes to the database.

### python shell
python manage.py shell

>>> from polls.models import Choice
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id

### create admin user
python3 manage.py createsuperuser

#### materials
https://docs.djangoproject.com/en/5.1/intro/tutorial02/

## views
Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.

### templates
load a template, 
fill a context and 
return an HttpResponse object with the result of the rendered template

## testing
1. test your code in shell
2. write automated tests and run 

python manage.py test polls

manage.py test polls looked for tests in the polls application

- it found a subclass of the django.test.TestCase class

- it created a special database for the purpose of testing

- it looked for test methods - ones whose names begin with test



# polls-app-django
