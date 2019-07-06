from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.core.validators import FileExtensionValidator

# # Data model for a request
# class Request(models.Model):
#     email = models.EmailField(max_length=64, default='')
#     input_file = models.FileField(
#         upload_to='./',
#         validators=[FileExtensionValidator(allowed_extensions=('txt', 'zip'))]
#     )
#     conf_file = models.FileField(upload_to='./')
#     request_time = models.CharField(max_length=30, default='')
#     status = models.CharField(max_length=30, default='new')
#     def __unicode__(self):
#         return self

# Data model for a request
class Request(models.Model):
    input_file = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=(['txt', 'zip']))]
    )
    email = models.EmailField(
        max_length=64,
    )
    max_context_lines = models.IntegerField(default=0)
    min_context_lines = models.IntegerField(default=0)
    ungram_kid_lines = models.IntegerField(default=0)
    input_ungram_distractors = models.IntegerField(default=0)
    output_ungram_distractor = models.IntegerField(default=0)
    ungram_num = models.IntegerField(default=0)
    nonsen_kid_words = models.IntegerField(default=0)
    input_nonsensical_distractors = models.IntegerField(default=0)
    nonsen_num = models.IntegerField(default=0)
    plau_kid_words = models.IntegerField(default=0)
    input_plau_distractors = models.IntegerField(default=0)
    output_plau_distractor = models.IntegerField(default=0)
    plau_num = models.IntegerField(default=0)

    request_time = models.CharField(max_length=30, default='')
    status = models.CharField(max_length=30, default='new')
    def __unicode__(self):
        return self

