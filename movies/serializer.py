from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    This class help us in converting movie queryset into JSON
    """
    class Meta:
        model = Movie
        fields = ('id', 'name', 'score')
