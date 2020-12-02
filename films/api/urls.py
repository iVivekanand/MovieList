from django.urls import path

from films.api.views import FilmListView, FilmDetailView

urlpatterns = [
    path('', FilmListView.as_view(), name='api'),
    path('<pk>', FilmDetailView.as_view())
]
