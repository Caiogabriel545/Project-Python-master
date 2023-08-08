from django.shortcuts import render

from django.http import HttpResponse

from .models import Movie

def home(request):
    seachMovie = request.GET.get('seachMovie')
    movies = Movie.objects.all()
    return render(request, 'home.html', {'seachMovie':seachMovie, 'movies': movies})


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})