from django.http import JsonResponse
from django.middleware.csrf import CsrfViewMiddleware


import logging
logger = logging.getLogger(__name__)

class Process500:
    def __init__(self, get_response):
        self._get_responce = get_response

    def __call__(self, request):
        return self._get_responce(request)

    def process_exception(self, request, exception):
        logger.error(request)
        logger.error(str(exception))
        print(str(exception))
        return JsonResponse({
            'success':False,
            'message':str(exception)
        })


class DisableCSRFMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        setattr(request, '_dont_enforce_csrf_checks', True)