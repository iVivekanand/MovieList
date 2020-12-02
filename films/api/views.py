from rest_framework.generics import ListAPIView, RetrieveAPIView

from films.models import Film
from .serializers import FilmSerializer

class FilmListView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetailView(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
