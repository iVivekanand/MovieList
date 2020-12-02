from django.db import models
from films.models.person import Person

class FilmManager(models.Manager):
    def create_film(self, id, title, description, release_date):
        film = self.create(
            id=id,
            title=title,
            description=description,
            release_date=release_date
        )
        return film


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
