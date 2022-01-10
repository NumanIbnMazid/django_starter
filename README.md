# Django Starter Template

## Description

Django Starter is a simple Skeleton for Django Project to start with.

## Installation

### Requirements

(click each one for install guide)

- [Python 3.8.x](http://docs.python-guide.org/en/latest/starting/installation/)
- [pip](https://pip.pypa.io/en/stable/installation/) or [poetry](https://python-poetry.org/docs/#installation)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Easy installation

1. Clone the git: `git clone https://github.com/NumanIbnMazid/django_starter.git`
2. Go into the new directory: `cd django_starter`

   ##### Install Dependencies Using Pip

   - Run `pip install -r requirements.txt`, this will install all the required dependencies.

     Please choose to (w)ipe if asked for this:

     ````
     The plan is to install the git repository https://github.com/XXXXXXXXXXXXXXXXXXXXXXXXXX
     What to do?  (i)gnore, (w)ipe, (b)ackup
     ````

   ##### Install Dependencies Using Poetry

   - Run `poetry install`, this will install all the required dependencies.

3. Create a `.env` file and provide required environment variables using the template `.env.example`
4. Run `python manage.py makemigrations` and `python manage.py migrate`, this will create the database tables
5. Run `python manage.py runserver`
    this should start the app on port 8000.
6. Open the app on browser by navigating the url `http://127.0.0.1:8000`

## Features

- [x] Easy Installation
- [x] Standard Project Structure
- [x] Example Landing Page using Bootstrap 5
- [ ] Setup script

## Author

- [Numan Ibn Mazid](https://github.com/NumanIbnMazid)
