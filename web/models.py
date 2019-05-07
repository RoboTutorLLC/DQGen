from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse

# Data model for a request
class Request(models.Model):
    email = models.EmailField(max_length=64, default='')
    input_file = models.FileField(upload_to='./')
    conf_file = models.FileField(upload_to='./')
    request_time = models.CharField(max_length=30, default='')
    status = models.CharField(max_length=30, default='new')
    def __unicode__(self):
        return self

