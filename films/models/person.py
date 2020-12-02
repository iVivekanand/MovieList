from django.db import models


class PersonManager(models.Manager):
    """
    Provides person object and meaningful name for foreign key
    """

    def create_person(self, id, name):
        person = self.create(
            id=id,
            name=name
        )
        return person

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Person(models.Model):
    """
    Schema definition for person, natural key exposed for human readability
    """
    id = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    objects = PersonManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name, )
