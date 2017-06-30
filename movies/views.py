import re

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import MoviesTrailer


class HomeView(View):
	""" Renders the website home page with movies traillers on it."""
	def get(self, request, *args, **kwargs):
		movies_entries = MoviesTrailer.objects.all()

		# It extracts the Youtube video ID from URL
		for movies in movies_entries:
			youtube_id_match = re.search(r'(?<=v=)[^&#]+', movies.trailer_url)
			youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movies.trailer_url)
			movies.trailer_url = youtube_id_match.group(0) if youtube_id_match else None

		context = {
			'title': 'Home',
			'movies': movies_entries
		}
		return render(request, 'movies/index.html', context)

class AboutView(View):
	""" Renders the website about page."""
	def get(self, request, *args, **kwargs):
		context = {
			'title': 'About',
		}
		return render(request, 'movies/about.html', context)
