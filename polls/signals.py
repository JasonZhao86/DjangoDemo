from django.core.signals import request_started, request_finished
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Choice
import django.dispatch

# def request_started_handler(sender, **kwargs):
#     print(sender, kwargs, "request_started")
#
# request_started.connect(request_started_handler)


@receiver(request_finished)
def request_finished_handler(sender, **kwargs):
    print("request_finished")

@receiver(post_save, sender=Choice)
def choice_handler(sender, **kwargs):
    print("pre_save")
    print("do something")


change_password_signal = django.dispatch.Signal(providing_args=['username'])

@receiver(change_password_signal)
def change_password_handler(sender, **kwargs):
    print("change password handler")