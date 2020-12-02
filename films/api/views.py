from rest_framework.generics import ListAPIView, RetrieveAPIView
from films.models.film import Film
from films.api.serializers.film_serializer import ListFilmSerializer, DetailFilmSerializer


class FilmListView(ListAPIView):
    """
    Serializer for list film view
    """
    queryset = Film.objects.all()
    serializer_class = ListFilmSerializer


class FilmDetailView(RetrieveAPIView):
    """
    Serializer for detailed film view
    """
    queryset = Film.objects.all()
    serializer_class = DetailFilmSerializer
