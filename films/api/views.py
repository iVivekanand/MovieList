from rest_framework.generics import ListAPIView, RetrieveAPIView
from films.models.film import Film
from films.api.serializers.film_serializer import ListFilmSerializer, DetailFilmSerializer


class FilmListView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = ListFilmSerializer


class FilmDetailView(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = DetailFilmSerializer
