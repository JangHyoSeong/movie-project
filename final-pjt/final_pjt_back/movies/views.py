from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    
    return render(request, 'movies/index.html', context)

def download_movie(request):
    return