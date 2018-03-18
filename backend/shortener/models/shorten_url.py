# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator

from shortener.managers import ShortenUrlManager
# Create your models here.
class ShortenUrl(models.Model):
    url = models.TextField(validators=[URLValidator()])
    shortcode = models.CharField(max_length=15, default="", unique=True, primary_key=True)
    created = models.DateTimeField(auto_now=True, blank=True)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True)
    
    objects = ShortenUrlManager()
    
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)