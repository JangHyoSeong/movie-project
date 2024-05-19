from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('v1/current_movies/', views.current_movies),
    path('v1/upcoming_movies/', views.upcoming_movies),
    path('v1/main/', views.main_view),
    path('v1/top_rated/', views.movie_sort_popularity),
    path('v1/movie/<str:movie_id>/', views.movie_detail),
    path('v1/choice/', views.choice),
]
