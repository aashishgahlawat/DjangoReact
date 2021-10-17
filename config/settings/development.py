# ./manage.py runserver --settings config.settings.development

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# INSTALLED_APPS = [
# ] + INSTALLED_APPS

# INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test2',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': 3307,
    }
}

# Your stuff...
# ------------------------------------------------------------------------------
