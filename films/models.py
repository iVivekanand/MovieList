from django.db import models


class FilmManager(models.Manager):
    def create_film(self, id, title, description, release_date):
        film = self.create(
            id=id,
            title=title,
            description=description,
            release_date=release_date
        )
        return film


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


class Film(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Person)

    objects = FilmManager()

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.title