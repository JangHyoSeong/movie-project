from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from ..models  import *


@api_view(['GET'])
def movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def main_view(request):
    if request.method == 'GET':
        serializer = ObjectCountSerializer()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)