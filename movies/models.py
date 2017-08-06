from django.db import models
from django.contrib.auth.models import User


class Director(models.Model):
    """
    class store details of directors
    """
    name = models.CharField(verbose_name="Name", max_length=30)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    class store list of genre
    """
    name = models.CharField(verbose_name="Name", max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    class contain details of movies.
    """
    name = models.CharField(verbose_name='Name', max_length=30)
    director = models.ForeignKey(Director, verbose_name="Director")
    genre = models.ManyToManyField(Genre, verbose_name="Genre", blank=True)
    score = models.IntegerField(verbose_name="Score",default=0)
    active = models.BooleanField(verbose_name="Is Active", default=True)
    creation_date = models.DateTimeField('Creation Date', auto_now_add=True)
    last_updated = models.DateTimeField('Last Updated', auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def search_movies(criteria, query):
        """
        This help us in searching for movie based criteria and query
        :param criteria: Criteria for search eg: genre, name
        :param query: Query for which to get match
        :return: QuerySet of movies
        """
        if not criteria:
            result_set = Movie.objects.filter(active=True)
        elif criteria == "Genre":
            result_set = Movie.objects.filter(active=True,
                                             genre__name__contains=query)
        elif criteria == 'Director':
            result_set = Movie.objects.filter(active=True,
                                             director__name__contains=query)
        else:
            result_set = Movie.objects.filter(active=True,
                                             name__contains=query)
        return result_set

    @staticmethod
    def movie_details(movie_id):
        """
        This method help us in getting detail of movie
        :param movie_id: Movie id for which need details
        :return: QuerySet containing movie detail
        """
        movie = Movie.objects.get(id=movie_id)
        genre = "\n".join([genre.name for genre in movie.genre.all()])
        director = movie.director.name
        result = {'genre': genre, 'director': director}
        return result


class UserMoviesWatchList(models.Model):
    """
    class stores user's movie interest
    """
    movie = models.ManyToManyField(Movie)
    user = models.ForeignKey(User)

    def __str_(self):
        return self.user.username

    @staticmethod
    def add_in_watchlist(user_id, movie_id):
        """
        This method help us in storing user movie watch list.
        :param movie_id: Movie id which to in watch list
        :return: Bool based on status
        """
        user_watchlist, created = UserMoviesWatchList.objects.get_or_create(user_id=int(user_id))
        movie = Movie.objects.get(id=movie_id)
        user_watchlist_movies = user_watchlist.movie.all()
        if movie not in user_watchlist_movies:
            user_watchlist.movie.add(movie)
            return "Movie saved"
        return "Already in watchlist"

    @staticmethod
    def get_recommendation():
        """
        This method help us in recommending movie for user
        :return: Queryset of movies recommended
        """
        pass

    @staticmethod
    def get_watchlist(user_id):
        """
        This method help us in getting watchlist of user
        :return: Queryset of movie of user's watch list
        """
        try:
            return UserMoviesWatchList.objects.get(user_id=int(user_id)).movie.all()
        except UserMoviesWatchList.DoesNotExist:
            return UserMoviesWatchList.objects.none()
