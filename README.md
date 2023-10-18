# Star Catalogue

This is a CRUD demonstration with Python, Django, HTML5, Bootstrap and Bootswatch with astral theme.

![plot](https://github.com/D-pyt/Python-CRUD-django/blob/master/stars/static/images/homepage.png?raw=true)



Install the following prerequisites:

1. [Python 3.8-3.11](https://www.python.org/downloads/)
2. [Django](https://docs.djangoproject.com/en/4.2/releases/4.2.5/)


## How to start

from **root**

1. Create venv

```
python -m venv venv
```
2. Activate venv

On mac:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Migrate db

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

5. Prepare admin user(superuser) in Django

```bash
python manage.py createsuperuser
```

follow setup and enter username, email and password.

6. Everything ready. Run the application

```bash
python manage.py runserver
```

Go to http://127.0.0.1:8000/ to view the application.
