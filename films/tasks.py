import requests

from threading import Thread
import time

from films.models import Film, Person


def update_films():
    films = requests.get('https://ghibliapi.herokuapp.com/films').json()
    people = requests.get('https://ghibliapi.herokuapp.com/people').json()
    existing_films = {
        existing_film.id: existing_film.title for existing_film in Film.objects.all()}
    for film in films:
        if film['id'] not in existing_films:
            new_film = Film.objects.create_film(
                film['id'], film['title'], film['description'], film['release_date']+'-01-01')
            new_film.save()
    existing_people = {
        existing_person.id: existing_person.name for existing_person in Person.objects.all()}
    for person in people:
        if person['id'] not in existing_people:
            new_person = Person.objects.create_person(
                person['id'], person['name'])
            new_person.save()
            for film in person['films']:
                Film.objects.get(id=film.split('/')[-1]).actors.add(new_person)


def update_database():
    while True:
        print('Updating films')
        update_films()
        print('Update done')
        time.sleep(60)

bg_thread = Thread(target=update_database, daemon=True)

def start_bg_task():
    if not bg_thread.is_alive():
        bg_thread.start()