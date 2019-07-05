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
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# import pdb


# handle DQGEn request
def home(request):
    context = {}
    context['form'] = RequestForm()
    print(f'context: {context}')
    return render(request, 'web/request.html', context)

# handle signup request
def handle_request(request):
    context = {}
    # pdb.set_trace()
    if request.method == 'GET':
        context['form'] = RequestForm()
        return render(request, 'web/request.html', context)

    try:        
        new_request = Request(
            email=request.POST['email'],
            input_file=request.FILES['input_file'],
            max_context_lines=request.POST['max_context_lines'],
            min_context_lines=request.POST['min_context_lines'],
            ungram_kid_lines = request.POST['ungram_kid_lines'],
            input_ungram_distractors = request.POST['input_ungram_distractors'],
            output_ungram_distractor = request.POST['output_ungram_distractor'],
            ungram_num = request.POST['ungram_num'],
            nonsen_kid_words = request.POST['nonsen_kid_words'],
            input_nonsensical_distractors = request.POST['input_nonsensical_distractors'],
            nonsen_num = request.POST['nonsen_num'],
            plau_kid_words = request.POST['plau_kid_words'],
            input_plau_distractors = request.POST['input_plau_distractors'],
            output_plau_distractor = request.POST['output_plau_distractor'],
            plau_num = request.POST['plau_num']
        )
        new_request.request_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        form_to_check = RequestForm(request.POST, instance=new_request)
        if form_to_check.is_valid():
            print('form valid')
        else:
            context['error'] = []
            for err in form_to_check.errors:
                context['error'].append(err)
            context['form'] = form_to_check
            # TODO: How to pass errors to render?
            return render(request, 'web/request.html', context)
        new_request.save()
        print(f'plau_num: {new_request.plau_num}')
        context['email'] = new_request.email
        context['input_file'] = new_request.input_file

        return render(request, 'web/back.html', context)
    except Exception as e:
        print(f'Exception: {e}')
        context['form'] = RequestForm()
        context['error'] = ["Request failed, please try again."]
        return render(request, 'web/request.html', context)

