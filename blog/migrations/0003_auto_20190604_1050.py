# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190604_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
