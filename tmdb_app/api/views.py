from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tmdb_app.models import Movie
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from tmdb_app.api.serializers import MovieSerializer

# Create your views here.
class MovieListAV(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class MovieDetailAV(APIView):
     def get(self, request,pk, format=None):
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    
     def put(self, request,pk, format=None):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
     def delete(self, request,pk, format=None):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
