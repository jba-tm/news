from .base import *
from django.utils.translation import ugettext_lazy as _

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '21a-f=x6$n7pxi4+e@m)7&be5squh@0y)lxx5ol7iv5ig_lye#'

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
