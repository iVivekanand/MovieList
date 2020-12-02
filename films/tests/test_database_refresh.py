from unittest import mock, TestCase
from django_mock_queries.query import MockSet, MockModel
from django.test import TestCase

from films.crons.database_refresh import fetch_people_from_ghibli_api, fetch_films_from_ghibli_api
from films.crons.database_refresh import update_people, update_films


class UpdateFilmAndPeopleTests(TestCase):
    films_qs = MockSet()
    people_qs = MockSet()

    def setUp(self):
        self.people_qs.add(
            MockModel(
                id="fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
                name="Pazu",
                films=[
                    "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
                ]
            )
        )
        self.films_qs.add(
            MockModel(
                id="2baf70d1-42bb-4437-b551-e5fed5a87abe",
                title="Castle in the Sky",
                description="The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
                release_date="1986"
            )
        )

    def _mock_response(self, json_data, status=200):
        mock_resp = mock.Mock()
        mock_resp.status_code = status
        mock_resp.json.return_value = json_data
        return mock_resp

    @mock.patch('requests.get')
    def test_fetch_people_from_ghibli_api(self, mock_get):
        """
        Check for valid get response
        """
        mock_get.return_value.ok = True

        response = fetch_people_from_ghibli_api()
        self.assertIsNotNone(response)

    @mock.patch('requests.get')
    def test_fetch_films_from_ghibli_api(self, mock_get):
        """
        Check for valid get response
        """
        mock_get.return_value.ok = True

        response = fetch_films_from_ghibli_api()
        self.assertIsNotNone(response)

    @mock.patch('films.models.film.Film.objects')
    @mock.patch('films.models.person.Person.objects')
    @mock.patch('requests.get')
    def test_update_people(self, mock_get, people_qs=MockSet(), films_qs=MockSet()):
        mock_resp = self._mock_response(self.people_qs)
        mock_get.return_value = mock_resp
        people_qs = self.people_qs
        films_qs = self.films_qs
        update_people()

    @mock.patch('films.models.film.Film.objects')
    @mock.patch('requests.get')
    def test_update_films(self, mock_get, films_qs=MockSet()):
        mock_resp = self._mock_response(self.films_qs)
        mock_get.return_value = mock_resp
        films_qs = self.films_qs
        update_films()
