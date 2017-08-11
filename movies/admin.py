from django.contrib import admin
from movies.models import Movie, Genre, Director
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    """
    This class used for handling all the request from admin.
    It handles request for movie creation, deletion and updation along with display.
    """
    list_display = ('name','score', 'director', 'get_genre_list')

    def get_queryset(self, request):
        qs = super(MovieAdmin, self).get_queryset(request)
        return qs.filter(active=True)

    def get_genre_list(self, obj):
        """
        Method use for getting genre data for every movie
        :param obj: queryset conataining movie
        :return: String with full list of genre
        """
        return "\n".join([genre.name for genre in obj.genre.all()])

    def delete_model(self, request, queryset):
        """
        This method handle delete movie requests.
        :param request:
        :param queryset:
        :return:
        """

        queryset.active = False
        queryset.save()



class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Director, DirectorAdmin)