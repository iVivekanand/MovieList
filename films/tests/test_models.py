from django.db import models
from django.test import TestCase

from films.models.person import Person, PersonManager
from films.models.film import Film, FilmManager


class FilmTestCases(TestCase):

    def test_create_film(self):
        class TestFilmManager(models.Model):
            objects = FilmManager()
        self.test_film_manager = TestFilmManager
        self.assertIsInstance(self.test_film_manager.objects, FilmManager)


class PersonTestCases(TestCase):

    def test_create_person(self):
        class TestPersonManager(models.Model):
            objects = PersonManager()
        self.test_person_manager = TestPersonManager
        self.assertIsInstance(self.test_person_manager.objects, PersonManager)
