from rest_framework import serializers

from .models import Watchlist,streamingPlatform

class WatchListSerializer(serializers.ModelSerializer):


	class Meta :
		model = Watchlist
		fields = '__all__'

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

	serializer = WatchListSerializer(many=True, read_only = True)
	class Meta :
		model = Watchlist
		fields = '__all__'