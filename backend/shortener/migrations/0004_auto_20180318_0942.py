# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20180318_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenurl',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shortenurl',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]