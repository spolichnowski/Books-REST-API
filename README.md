# Books REST API

> 

## Technologies

- Django
- Django REST framework
- PostgreSQL

## Setup

### To run the application:

Prepare virtual environment, for example with:
- venv (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

After creating and running your virtual environment make sure that your 'pip' package installer is working. Check its version for a test and if needed update it:

```
$ pip --version
$ pip install --upgrade pip
```

Now time to install all the requirements:

```
$ cd ../project folder/backend
$ pip install -r requirements.txt
```

Then run application:

```
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```
