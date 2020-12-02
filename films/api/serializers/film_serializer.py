from rest_framework import serializers

from films.models.film import Film
from films.api.serializers.person_serializer import PersonSerializer


class ListFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title')


class DetailFilmSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(many=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'description', 'release_date', 'actors')
        use_natural_foreign_keys = True
