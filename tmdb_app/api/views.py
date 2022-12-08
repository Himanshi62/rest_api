from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tmdb_app.models import Movie
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from tmdb_app.api.serializers import MovieSerializer

# Create your views here.
@api_view()
def list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True)
    return Response(serializer.data)


@api_view()
def movie_detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
