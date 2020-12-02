from rest_framework import serializers

from films.models import Film, Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'id')

class FilmSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(many=True)
    class Meta:
        model = Film
        fields = ('title', 'description', 'release_date', 'actors')
        use_natural_foreign_keys=True