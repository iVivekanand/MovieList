from django.contrib import admin
from django.urls import path, include

from films.crons.database_refresh import start_db_refresh
from films.views import home

urlpatterns = [
    path('movies/', home, name='home'),
    path('movies/api/', include('films.api.urls')),
]

start_db_refresh()