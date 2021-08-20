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

## or

### Docker-compose

    docker-compose up --build

run migrations 

    docker-compose exec web python manage.py migrate


If you need to scale service, you can set up extra instances of apps and configure load balancer to use them all.
