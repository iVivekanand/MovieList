from django.contrib import admin
from django.urls import path, include

from films.crons.database_refresh import start_db_refresh
from films.views import home

urlpatterns = [
    path('', admin.site.urls),
    path('movies/', home, name='home'),
    path('movies/api/', include('films.api.urls')),
]

# Backgroung daemon to be started during server startup
start_db_refresh()
