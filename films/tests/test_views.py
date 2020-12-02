from django.test import TestCase, Client
from django.http import request
from django.urls import reverse

class TestViews(TestCase):

    def test_home_movie_list(self):
        client = Client()

        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')