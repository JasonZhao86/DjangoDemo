from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     USER_ROLE_CHOICES = (
#         ('SU', 'SuperUser'),
#         ('GA', 'GroupAdmin'),
#         ('CU', 'CommonUser'),
#     )
#
#     name = models.CharField(max_length=80)
#     uuid = models.CharField(max_length=100)
#     role = models.CharField(max_length=2, choices=USER_ROLE_CHOICES, default='CU')
#     ssh_key_pwd = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name