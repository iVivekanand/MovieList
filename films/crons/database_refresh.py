import requests
import time
import threading

from threading import Thread

from films.models.film import Film
from films.models.person import Person
from films.constants import FILM_API_URL, PEOPLE_API_URL


def fetch_people_from_ghibli_api():
    return requests.get(PEOPLE_API_URL).json()


def fetch_films_from_ghibli_api():
    return requests.get(FILM_API_URL).json()


def update_films():
    films = requests.get(FILM_API_URL).json()
    existing_films = {
        existing_film.id: existing_film.title for existing_film in Film.objects.all()}
    for film in films:
        if film['id'] not in existing_films:
            new_film = Film.objects.create_film(
                film['id'], film['title'], film['description'], film['release_date']+'-01-01')
            new_film.save()


def update_people():
    people = requests.get(PEOPLE_API_URL).json()
    existing_people = {
        existing_person.id: existing_person.name for existing_person in Person.objects.all()}
    for person in people:
        if person['id'] not in existing_people:
            new_person = Person.objects.create_person(
                person['id'], person['name'])
            new_person.save()
            for film in person['films']:
                Film.objects.get(id=film.split('/')[-1]).actors.add(new_person)


def update_databases():
    threading.Timer(60, update_databases).start()
    print('Updating films')
    update_films()
    print('Film update done')
    print('Updating people')
    update_people()
    print('People update done')


thread_db_refresh = Thread(target=update_databases, daemon=True)


def start_db_refresh():
    if not thread_db_refresh.is_alive():
        thread_db_refresh.start()
