from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('v1/movies/', views.movies),
    path('v1/main/', views.main_view),
]
