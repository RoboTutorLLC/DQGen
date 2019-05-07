from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.db import transaction
from django.conf import settings
from web.models import *
from web.forms import *
import datetime
import os
import time
import json


# handle DQGEn request
def home(request):
    context = {}
    context['form'] = RequestForm()
    return render(request, 'web/request.html', context)

# handle signup request
def handle_request(request):
    context = {}
    if request.method == 'GET':
        context['form'] = RequestForm()
        return render(request, 'web/request.html', context)

    try:
        new_request = Request(email=request.POST['email'],
                              input_file=request.FILES['input_file'],
                              conf_file=request.FILES['conf_file'])
        new_request.request_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_request.save()
        context['email'] = new_request.email
        return render(request, 'web/back.html', context)
    except Exception as e:
        context['form'] = RequestForm()
        context['error'] = "Request failed, try again!"
        return render(request, 'web/request.html', context)

