# ./manage.py collectstatic
# ./manage.py check --deploy

from .base import *
from decouple import Csv


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS = ['happyhome.com', 'www.happyhome.com']
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Get code error notification
# ADMINS = [("aashish", "aashishgahlawat9@gmail.com"), ]
ADMINS = config('ADMIN', cast=Csv(post_process=tuple))

# Get broken links notification
MANAGERS = ADMINS

# Reading SECRET_KEY from secret_key.txt file rather than directly saving it to settings.py
# secret_key.txt shall include only value (even without quotes and SECRET_KEY word)

# with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
#     SECRET_KEY = f.read().strip()

# DATABASES = {
#     'default': config(
#         'DATABASE_URL',
#         default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
#         cast=db_url
#     )
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}

# HTTPS settings
SESSION_COOKIES_SECURE = True
CSRF_COOKIES_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS (http strict transport security) settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
#
# EMAIL_BACKEND = ''
# EMAIL_HOST = ''
# EMAIL_PORT = ''
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = ''

# Your stuff...
# ------------------------------------------------------------------------------
