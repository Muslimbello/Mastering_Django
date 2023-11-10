from django.urls import path
from .views import watchlistAV , streamplatformAV, watchlistDetails

urlpatterns = [
	path('watchlist/', watchlistAV, name= 'watchlist'),
	path('watchlist/<int:pk>/', watchlistDetails, name= 'watchlist-details'),

	path('streamplatform/', streamplatformAV, name= 'stream')
]