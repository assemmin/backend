from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False)

def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
        return JsonResponse({
            "title": movie.title,
            "description": movie.description,
            "producer": movie.producer,
            "duration": movie.duration,
        })
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Movie not found"}, status=404)

# Create your views here.
