from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%#qw8hwz2xw5ioje@l#f3g1l2qzg916xn5fpaza(6ap=fzntj%'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

