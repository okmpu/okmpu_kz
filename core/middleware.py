from django.utils import translation
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class AllowIframeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'X-Frame-Options' in response:
            del response['X-Frame-Options']
        return response


class CustomLocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        language = request.session.get('django_language') or request.COOKIES.get('django_language')

        if not language:
            language = 'kk'

        translation.activate(language)
        request.LANGUAGE_CODE = language