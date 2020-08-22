from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'g&#y4)nawrii92s%=(hgwrb2&ph&k1n2kmu=i75t_737__=j-1'

WAGTAIL_SITE_NAME = _('World news')

# Session settings
# SESSION_COOKIE_SECURE = True
#
# # Publish settings
SECURE_SSL_REDIRECT = False
#
# SECURE_HSTS_SECONDS = 3600
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
#
# SECURE_CONTENT_TYPE_NOSNIFF = True
#
# SECURE_BROWSER_XSS_FILTER = True

# CSRF_COOKIE_SECURE = True

# X_FRAME_OPTIONS = "DENY"
#
# SECURE_REFERRER_POLICY = 'origin'

try:
    from .local import *
except ImportError:
    pass
