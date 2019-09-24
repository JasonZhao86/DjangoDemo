from django.http import HttpResponse
import os

IN_DEMO_MODE = os.environ.get('DEMO_MODE', False)
SAFE_METHOD = ('GET', 'HEAD')
SAFE_URL = ('/polls/login/')

class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if IN_DEMO_MODE and request.method not in SAFE_METHOD and request.path not in SAFE_URL:
            return HttpResponse("In demo mode, only safe method only")
        response = self.get_response(request)
        return response