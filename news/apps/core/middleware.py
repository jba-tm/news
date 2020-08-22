from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django import VERSION as DJANGO_VERSION
from django.utils import deprecation

from importlib import import_module

from news.apps.core.models import Visitor, OnlineUserActivity

engine = import_module(settings.SESSION_ENGINE)

################
# Online users #
################


class OnlineNowMiddleware(MiddlewareMixin):
    """Updates the OnlineUserActivity database whenever an authenticated user makes an HTTP request."""

    # def __init__(self, get_response):
    #     self.get_response = get_response
    #     # One-time configuration and initialization.
    #
    # def __call__(self, request):
    #     # Code to be executed for each request before
    #     # the view (and later middleware) are called.
    #
    #     response = self.get_response(request)
    #
    #     # Code to be executed for each request/response after
    #     # the view is called.
    #
    #     return response

    def process_request(self, request):
        user = request.user
        if not user.is_authenticated:
            return
        ip_address = self.get_ip_address(request)
        OnlineUserActivity.update_user_activity(user, ip_address)

    @staticmethod
    def get_ip_address(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


############################
# Prevent concurrent login #
############################


def is_authenticated(user):
    """
    Check if user is authenticated, consider backwards compatibility
    """
    if DJANGO_VERSION >= (1, 10, 0):
        return user.is_authenticated
    else:
        return user.is_authenticated()


class PreventConcurrentLoginMiddleware(deprecation.MiddlewareMixin if DJANGO_VERSION >= (1, 10, 0) else object):
    """
    Django middleware that prevents multiple concurrent logins..
    Adapted from http://stackoverflow.com/a/1814797 and https://gist.github.com/peterdemin/5829440
    """
    @staticmethod
    def process_request(request):
        if is_authenticated(request.user):
            key_from_cookie = request.session.session_key
            if hasattr(request.user, 'visitor'):
                session_key_in_visitor_db = request.user.visitor.session_key
                if session_key_in_visitor_db != key_from_cookie:
                    # Delete the Session object from database and cache
                    engine.SessionStore(session_key_in_visitor_db).delete()
                    request.user.visitor.session_key = key_from_cookie
                    request.user.visitor.save()
            else:
                Visitor.objects.create(
                    user=request.user,
                    session_key=key_from_cookie
                )
