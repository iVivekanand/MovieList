from rest_framework import serializers

from films.models.film import Film
from films.api.serializers.person_serializer import PersonSerializer


class ListFilmSerializer(serializers.ModelSerializer):
    """
    Expose ID and title in list view
    """
    class Meta:
        model = Film
        fields = ('id', 'title')


class DetailFilmSerializer(serializers.ModelSerializer):
    """
    Show ID, title, description, release date and actor details

    Actor information is retrieved from Person model
    """
    actors = PersonSerializer(many=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'description', 'release_date', 'actors')
        use_natural_foreign_keys = True
