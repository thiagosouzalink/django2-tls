import environ

from django2.settings.base import *
#import dj_database_url


# Instância de ENV
env = environ.Env()

# Set DEBUG = False no Heroku
DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    #'default': dj_database_url.config()
    "default": env.db(),
}