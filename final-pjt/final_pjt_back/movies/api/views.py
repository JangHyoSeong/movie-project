from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from ..models  import *

# HomeView.vue 영화 포스터
@api_view(['GET'])
def movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by('-review_score').filter(show_status=0))[:10]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def main_view(request):
    if request.method == 'GET':
        data = {}
        serializer = ObjectCountSerializer(data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def movie_sort_popularity(request):
    movies = Movie.objects.filter(Q(show_status=0) | Q(show_status=2)).order_by('-popularity')
    serializer = MovieListSummarySerializer(movies, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = MovieDetailSerializer(movie)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def choice(request):
    movies = get_list_or_404(Movie)[:10]
    genres = get_list_or_404(Genre)[:10]
    countries = get_list_or_404(Country)[:10]
    actors = get_list_or_404(Actor)[:10]
    producers = get_list_or_404(Producer)[:10]
    
    data = {
        'movies': movies,
        'genres': genres,
        'actors': actors,
        'countries': countries,
        'producers': producers,
    }
    serializer = ChoiceSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)