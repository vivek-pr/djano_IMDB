from django.shortcuts import render
from movies.models import Movie, UserMoviesWatchList
from movies.serializer import MovieSerializer
from django.http import JsonResponse
import json


def home(request):
    queryset = Movie.search_movies(None, None)
    serializer = MovieSerializer(queryset, many=True)
    return render(request, 'base.html',
                  context={'movies_list': json.dumps(serializer.data)})


def search_movies(request):
    """
    This method help us in getting movie list based on our search criteria.
    In case of no search request, it returns full movie list
    :param request: Http Request object
    :param criteria: criteria for search query eg.genre, name, director
    :param query: string for which, to search for
    :return: JSON of Queryset of movies
    """
    criteria = request.GET.get("criteria", None)
    query = request.GET.get('query', None)
    queryset = Movie.search_movies(criteria, query)
    serializer = MovieSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


def movie_details(request):
    """
    This method help us in getting detail of a Movie.
    :param request: Http Request object
    :param movie_id: Id of movie
    :return: Json containing details of movie
    """
    movie_id = request.GET.get('movie_id')
    queryset = Movie.movie_details(movie_id)
    # serializer = MovieSerializer(queryset)
    return JsonResponse(queryset)


def add_in_watchlist(request):
    """
    This method help us in adding a movie in watchlist.
    :param request: Http Request object
    :param movie_id: Movie id which will be saved in watch list
    :return: True or False based on task status
    """
    movie_id = request.GET.get("movie_id")
    status = UserMoviesWatchList.add_in_watchlist(request.user.id,
                                                  movie_id)
    return JsonResponse(status, safe=False)


def get_watchlist(request):
    """
    This method help us in getting the list of movies added by user in watchlist
    :param request: Http Request object
    :return: JSON of movie list from watchlist
    """
    queryset = UserMoviesWatchList.get_watchlist(request.user.id)
    serializer = MovieSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

