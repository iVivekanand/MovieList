import threading
import time

from . import tasks

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include('films.api.urls')),
]

tasks.start_bg_task()