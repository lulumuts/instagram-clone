# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 13:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20180516_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
