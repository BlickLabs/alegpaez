# Alegpaez Project

## Previous requirements
* Wordpress instance running

## Setup

* This project uses python 2.7
* Install [virtualenv](https://virtualenv.pypa.io/en/stable/) and read how to create and activate a virtualenv
* On an active virtualenv install the local requirements `pip install -r requirements/local.txt`
* Export the vars on the .env file, on the engine option use `django.db.backends.mysql` for mysql or `django.db.backends.postgresql` for psq, for more reference check this [link](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-DATABASE-ENGINE). The vars with DB_DEFAULT_* refears to the project database, the vars with DB_WORDPRESS_* refears to the wordpress database instace
* Run `python manage.py migrate --database=default`
* Create a superuser for the admin `python manage.py createsuperuser --database=default`
* Run project using `python manage.py runserver 8000`
* Go to [localhost:8000](localhost:8000) to see the project, the admin is in [localhost:8000/admin](localhost:8000/admin)

If you have published post on the wordpress instace, you will se some data in the project homepage