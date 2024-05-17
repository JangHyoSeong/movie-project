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
    country_count = serializers.SerializerMethodField()

    def get_movie_count(self, obj):
        return Movie.objects.count()
    
    def get_genre_count(self, obj):
        return Genre.objects.count()
    
    def get_producer_count(self, obj):
        return Producer.objects.count()
    
    def get_actor_count(self, obj):
        return Actor.objects.count()
    
    def get_country_count(self, obj):
        return Country.objects.count()
    

class MovieListSummarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'poster', 'popularity', )
        
        
class MovieDetailSerializer(serializers.ModelSerializer):
    
    class MovieSnapshotSerializer(serializers.ModelSerializer):
        class Meta:
            model = Snapshot
            fields = ('snapshot',)
            
    class MovieActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
            
    class MovieProducerListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Producer
            fields = '__all__'
            
    actor = MovieActorListSerializer(many=True, read_only=True)
    snapshots = MovieSnapshotSerializer(many=True, read_only=True)
    producer = MovieProducerListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'