from __future__ import unicode_literals
from django.contrib import messages
from django.http import JsonResponse

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class WagtailenforcerMiddleware(MiddlewareMixin):

    """
    Provides full logging of requests and responses
    """
    _initial_http_body = None

    def process_request(self, request):
        self._initial_http_body = request.body # this requires because for some reasons there is no way to access request.body in the 'process_response' method.

    def process_exception(self, request, exception):
        """
        Catch raised validation exception
        """
        if type(exception).__name__ == 'EnforcerVirusException':
            return JsonResponse({
                'success': False,

                # https://github.com/django/django/blob/stable/1.6.x/django/forms/util.py#L45
                'error_message': exception.message,
            })
