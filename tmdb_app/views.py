from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Movie


# Create your views here.
def list(request):
    movies = Movie.objects.all()
    movie_list =[]
    for obj in movies:
        movie_list.append({
            "id" : obj.pk,
            "name" : obj.name,
            "description" : obj.description,
            "release_date" : obj.release_date,
            "isHit" : obj.isHit
        })
    dic = {
        "movies" : movie_list
    }
    print(dic["movies"])
    return JsonResponse(dic)

def movie_detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    dic = {
        "name" : movie.name,
        "description" : movie.description,
        "release_date" : movie.release_date,
        "isHit" : movie.isHit
    }
    return JsonResponse(dic)