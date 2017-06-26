from django.db import models


class MoviesTrailer(models.Model):
	name = models.CharField(max_length=100)
	year = models.IntegerField()
	sinopse = models.CharField(max_length=300)
	category = models.CharField(max_length=15)
	trailer_url = models.CharField(max_length=200)

	def __str__(self):
		return str(self.name)

	def get_movie_trailer(self):
		return self.trailer_url
