# DjangoMySQL
Basics of building REST API in Django.

## Prerequisites
* [Python](https://www.python.org/downloads/) (Version 3.9+)
* [virtualenv](https://pypi.org/project/virtualenv/) `pip install virtualenv`

## Installation
* Create and activate virtual environtment (for Windows)
```
virtualenv env
./env/Scripts/activate
```

* Create a `config.ini` file in the root directory and add the following (with your own configuration) in the file
```
[mysql]
username = <your_db_username>
password = <your_db_password>
hostname = <your_db_hostname>
port = <your_db_port>
db_name = <your_db_name>
[django]
secret_key = <your_django_secret_key>
```

(for commands below make sure the env is activated)

* Install requirements
```
pip install -r requirements.txt
```

* Migrate database
```
cd app
python manage.py migrate
```


## Build and Run
* Start django server
```
cd app
python manage.py runserver 8000
```


## Dev
(Reminders for commands and stuff used during developement.)
* Start Django project
```
cd app
django-admin startproject app .
```

* Run Django server
```
cd app
python manage.py runserver 8000
```

* Create API app
```
cd app
python manage.py startapp api
```

* add `api` in `app/app/settings.py` inside `INSTALLED_APPS`
* Create api in `app/api/views.py`

* Create products app
```
cd app
python manage.py startapp products
```

* migration (lets the database know about everything thats happeining in model)
```
cd app
python manage.py makemigrations
python manage.py migrate
```
