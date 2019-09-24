from django.conf.urls import url
from .views import proxy_forward

urlpatterns = [
    # url(r'^blog/$'),
    url(r'^kibana/', proxy_forward),
]