from rest_framework import serializers
from ..models import *

class MovieListSerializer(serializers.ModelSerializer):
    
    class ActorNameSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Actor
            fields = ('actor', )
    
    actor = ActorNameSerializer(many=True, read_only=True)    
      
    class Meta:
        model = Movie
        fields = '__all__'
        
class ObjectCountSerializer(serializers.Serializer):
    movie_count = serializers.SerializerMethodField()
    genre_count = serializers.SerializerMethodField()
    producer_count = serializers.SerializerMethodField()
    actor_count = serializers.SerializerMethodField()

    def get_movie_count(self, obj):
        return Movie.objects.count()
    
    def get_genre_count(self, obj):
        return Genre.objects.count()
    
    def get_producer_count(self, obj):
        return Producer.objects.count()
    
    def get_actor_count(self, obj):
        return Actor.objects.count()
    

class MovieListSummarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'poster', 'popularity', )