from django.http import HttpRequest, HttpResponse

def index(request):
    return HttpResponse('Welcome to index page')

def static(request):
    return HttpResponse("/static/")