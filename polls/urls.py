from django.conf.urls import url
from .views import Index, question_choice, Voting, result, send_email
from .views import download_csv, download_file, upload_file, auth_login, auth_logout

# app_name = "polls"

urlpatterns = [
    url(r'^login/$', auth_login, name='auth_login'),
    url(r'^logout/$', auth_logout, name='auth_logout'),
    url(r'^index/$', Index.as_view(), name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', Voting.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/choice/$', question_choice, name='choice'),
    url(r'^(?P<question_id>[0-9]+)/voting/$', Voting.as_view(), name='voting'),
    url(r'^(?P<question_id>[0-9]+)/result/$', result, name='result'),
    url(r'^email/$', send_email, name="email"),
    url(r'^csv/$', download_csv, name="csv"),
    url(r'^upload/$', upload_file, name="upload"),
    url(r'^download/$', download_file, name="download"),
]