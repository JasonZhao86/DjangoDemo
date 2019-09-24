from django.conf.urls import url
from .views import PublisherAdd, PublisherDetail, PublisherUpdate, PublisherDelete ,AboutView
from .views import GreetingView, MorningGreetingView, PubliserList, ContactUs

urlpatterns = [
    url(r'^add/$', PublisherAdd.as_view(), name="publisher_add"),
    url(r'^update/(?P<pk>[0-9]+)/$', PublisherUpdate.as_view(), name="publisher_update"),
    url(r'^delete/(?P<pk>[0-9]+)/$', PublisherDelete.as_view(), name="publisher_delete"),
    url(r'^(?P<pk>[0-9]+)/$', PublisherDetail.as_view(), name="publisher_detail"),
    url(r'^email/$', ContactUs.as_view(), name="contact_us"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^greeting/$', GreetingView.as_view(), name="GreetingView"),
    # url(r'^moring_greeting/$', MorningGreetingView.as_view(), name="MorningGreetingView"),
    url(r'^moring_greeting/$', MorningGreetingView.as_view(greeting="Hello Guy"), name="MorningGreetingView"),
    url(r'^publisher_list/$', PubliserList.as_view(), name="publisher_list"),
]