Shortener API
---------------------------

#### Setup environment

create .env file in root project dir (from env.example):

    cp .env.example .env

#### Create database

from .env file configuration:

    (source .env && eval "echo \"$(cat tools/sql/create_db.sql)\"") | psql

#### Install requirements

    pip install -r requirements.txt

or  

Docker-compose

    docker-compose up --build


run migrations
    
    python manage.py migrate

or via docker

    docker-compose exec web python manage.py migrate

create superuser

    python manage.py createsuperuser

or via docker

    docker-compose exec web createsuperuser

in admin app http://127.0.0.1:8000/admin/sites/site/ add local site

    http://127.0.0.1:8000/

swagger endpoint http://127.0.0.1:8000/docs/


###for endpoint /shortener url shoud starts with http:// or https:// like: https://www.helloworld.com

If you need to scale service, you can set up extra instances of apps and configure load balancer to use them all.
