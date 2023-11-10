from django.shortcuts import render
from rest_framework import generics
from .models import Watchlist, streamingPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
# Create your views here.

class watchlistAV(generics.ListCreateAPIView):
	queryset  = Watchlist.objects.all()
	serializer_class = WatchListSerializer

class streamplatformAV(generics.ListCreateAPIView):
	queryset  = streamingPlatform.objects.all()
	serializer_class = StreamPlatformSerializer

class watchlistDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset  = Watchlist.objects.all()
	serializer_class = WatchListSerializer