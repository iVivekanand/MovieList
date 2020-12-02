from django.urls import path

from .views import FilmListView, FilmDetailView

urlpatterns = [
    path('', FilmListView.as_view()),
    path('<pk>', FilmDetailView.as_view())
]