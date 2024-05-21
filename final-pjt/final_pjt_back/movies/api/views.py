from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from django.contrib.auth import get_user_model
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
def current_movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by('-review_score').filter(show_status=0, review_score__lt=9.5))[:10]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def upcoming_movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by('-review_score').filter(show_status=1, review_score__lt=9.5))[:10]
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
    movies = Movie.objects.filter(
        Q(genre__isnull=False) & Q(country__isnull=False) & Q(producer__isnull=False)
    ).distinct()
    genres = get_list_or_404(Genre)
    countries = get_list_or_404(Country)
    actors = get_list_or_404(Actor)
    producers = get_list_or_404(Producer)
    
    data = {
        'movies': movies,
        'genres': genres,
        'actors': actors,
        'countries': countries,
        'producers': producers,
    }
    serializer = ChoiceSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def choice_result(request):
    genre = request.query_params.get('genre')
    country = request.query_params.get('country')
    actor = request.query_params.get('actor')
    producer = request.query_params.get('producer')
    
    query = Q()
    if genre is not None:
        query &= Q(genre=genre)
    if country is not None:
        query &= Q(country=country)
    if actor is not None:
        query &= Q(actor=actor)
    if producer is not None:
        query &= Q(producer=producer)
    
    queried_movies = Movie.objects.filter(query).order_by('-review_score')
    serializer = MovieSerializer(queried_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def review(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    if request.method == 'GET':
        reviews = get_list_or_404(MovieReview, movie=movie)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user = get_object_or_404(get_user_model(), username=request.user)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == 'DELETE':
        print(request.data)
        review = get_object_or_404(MovieReview, id=request.data.get('review_id'))
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def current_user(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_profile(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    serializer = UserSerializer()
    
@api_view(['GET', 'POST'])
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    user = get_object_or_404(get_user_model(), username=request.user)
    
    if request.method == 'POST':
        if user in movie.like_users.all():
            movie.like_users.remove(user)
        else:
            movie.like_users.add(user)
            
        return Response(status=status.HTTP_202_ACCEPTED)
    
    elif request.method == 'GET':
        serializer = MovieLikeSerializer(movie, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_associate(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    genres = movie.genre.all()
    related_movies = Movie.objects.filter(genre__in=genres, review_score__lt=9.4).exclude(movie_id=movie_id).distinct().order_by('-review_score')[:6]
    serializer = MovieListSerializer(related_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def movie_chat(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    user = get_object_or_404(get_user_model(), username=request.user)
    
    if request.method == 'GET':
        chats = get_list_or_404(MovieChat, movie=movie)
        serializer = MovieChatSerialzier(chats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user = get_object_or_404(get_user_model(), username=request.user)
        serializer = MovieChatSerialzier(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def profile(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    serializer = UserProfileSerializer(user)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def profile_review(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    movies = Movie.objects.filter(request.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def member_leave(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)