
from django.contrib import admin
from django.urls import path, include
from  . import views

urlpatterns = [
    path("list", views.MovieListAV.as_view(), name="movielist"),
    path("list/<int:pk>",views.MovieDetailAV.as_view(), name="MovieDetailAV")
]
