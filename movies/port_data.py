import json
from movies.models import Movie, Director, Genre


def port_data():
    with open('/home/ubuntu/djano_IMDB/imdb.json') as data_file:
        movies_data = json.load(data_file)

    for movie in movies_data:
        movie_name = movie["name"]
        movie_director = movie["director"]
        movie_genre = movie["genre"]
        movie_score = movie["imdb_score"]
        director, created = Director.objects.get_or_create(name=movie_director)
        movie_created = Movie.objects.create(name=movie_name,
                                             director=director,
                                             score=movie_score)
        for genre in movie_genre:
            genre_check, created = Genre.objects.get_or_create(name=genre)
            movie_created.genre.add(genre_check)
