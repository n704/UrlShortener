# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20180318_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]