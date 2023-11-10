from django.db import models

# Create your models here.

class streamingPlatform(models.Model):
	name = models.CharField(max_length=50)
	about = models.CharField(max_length=200)
	website = models.URLField(max_length=100)

	def __str__(self):
		return self.name

class Watchlist(models.Model):
	title = models.CharField(max_length=200)
	storyline = models.CharField(max_length=100)
	createdby = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	streamingPlatform = models.ForeignKey(streamingPlatform, on_delete=models.CASCADE, related_name='')

	def __str__(self):
		return self.title


