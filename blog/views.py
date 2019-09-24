from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import requests

def proxy_forward(request):
    # r = requests.get("https://54.223.238.167", auth=('hpbridge', 'Kr4&T0m#szgy7s'), verify=False)
    r = requests.get("https://www.baidu.com/")
    # print(r.status_code)
    # print(r.text)
    return HttpResponse(r)

# proxy_forward(1)
