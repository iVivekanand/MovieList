import requests
import time
import threading

from threading import Thread

from films.models.film import Film
from films.models.person import Person
from films.constants import FILM_API_URL, PEOPLE_API_URL


def fetch_people_from_ghibli_api():
    """
    Query people details from external API
    """
    return requests.get(PEOPLE_API_URL).json()


def fetch_films_from_ghibli_api():
    """
    Query film details from external API
    """
    return requests.get(FILM_API_URL).json()


def update_films():
    """
    Update film to block storage if not already present
    As only release year is received from API, the equivalent field is updated
    with 01-01 (dd-mm) to convert to datefield
    """
    films = requests.get(FILM_API_URL).json()
    existing_films = {
        existing_film.id: existing_film.title
        for existing_film in Film.objects.all()
    }
    for film in films:
        if film['id'] not in existing_films:
            new_film = Film.objects.create_film(
                film['id'],
                film['title'],
                film['description'],
                film['release_date'] + '-01-01'
            )
            new_film.save()


def update_people():
    """
    Update people to block storage if not already present
    Once all people information are updated, loop through movies to update cast
    Update people should be invoked only after update films as people data in 
    films API is broken and correct film information is available in people api
    """
    people = requests.get(PEOPLE_API_URL).json()
    existing_people = {
        existing_person.id: existing_person.name
        for existing_person in Person.objects.all()
    }
    for person in people:
        if person['id'] not in existing_people:
            new_person = Person.objects.create_person(
                person['id'],
                person['name']
            )
            new_person.save()
            for film in person['films']:
                Film.objects.get(id=film.split('/')[-1]).actors.add(new_person)


def update_databases():
    """
    A background thread that runs every minute to update backend data
    """
    threading.Timer(60, update_databases).start()
    print('Updating films')
    update_films()
    print('Film update done')
    print('Updating people')
    update_people()
    print('People update done')


thread_db_refresh = Thread(target=update_databases, daemon=True)


def start_db_refresh():
    """
    Ensures only a single parallel thread for db update
    """
    if not thread_db_refresh.is_alive():
        thread_db_refresh.start()
