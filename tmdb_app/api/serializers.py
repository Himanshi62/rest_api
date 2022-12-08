from rest_framework import serializers
from tmdb_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    release_date = serializers.CharField()
    isHit = serializers.BooleanField()