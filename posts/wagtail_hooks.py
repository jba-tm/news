from wagtail.core import hooks
from django.contrib.auth.models import Permission


@hooks.register('register_permissions')
def save_post_as_pdf():
    return Permission.objects.filter(codename='save_post_as_pdf')
