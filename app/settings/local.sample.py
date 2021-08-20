from .common import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # fill from .env
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost', #or 'db' if docker
        'PORT': os.getenv('POSTGRES_PORT', 5432)
    }
}

AUTH_DEBUG = True
