from rest_framework import serializers
from films.models.person import Person


class PersonSerializer(serializers.ModelSerializer):
    """
    Expose ID and name for person details.

    Further details can be exposed based on need
        Gender, age, eye/hair color, species, films
    """
    class Meta:
        model = Person
        fields = ('name', 'id')
