from django.db import models


class PersonManager(models.Manager):
    def create_person(self, id, name):
        person = self.create(
            id=id,
            name=name
        )
        return person

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Person(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    objects = PersonManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name, )
