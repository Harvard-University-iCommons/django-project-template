from .base import *
from logging.config import dictConfig

DEBUG = True

SECRET_KEY = '{{ secret_key }}'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS.extend(['django_extensions'])

INSTALLED_APPS.extend(['debug_toolbar'])
MIDDLEWARE.extend(['debug_toolbar.middleware.DebugToolbarMiddleware'])

# For Django Debug Toolbar:
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
