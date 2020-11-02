from .base import *
from django.utils.translation import ugettext_lazy as _

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


WAGTAIL_SITE_NAME = _('World news test server')

BASE_URL = 'http://news.loc'

# Session settings
CSRF_USE_SESSIONS = True

CSRF_COOKIE_HTTPONLY = True

try:
    from .local import *
except ImportError:
    pass
