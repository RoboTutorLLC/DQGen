import sys
import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls import *
from django.conf.urls.static import static

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns = [
    re_path(r'^handle_request$', views.handle_request, name='handle_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.append(re_path(r'^.*$', views.home, name='home'))
