from films.models.film import Film
from django.shortcuts import render

def home(request):
    films_in_db = Film.objects.all()
    films = {}
    for film in films_in_db:
        actors = set()
        film_details = {
            'title': film.title,
            'description': film.description,
            'release_date': film.release_date,
            'actors': [actor.name for actor in film.actors.all()]
        }
        if not film_details['actors']:
            film_details['actors'].append('Not available')
        films[film.id] = film_details

    return render(request, 'index.html', {
        'films': films
    })