from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import MoviesTrailer

class HomeView(View):
	""" Renders the website home page with movies traillers on it."""
	def get(self, request, *args, **kwargs):
		movies_entries = MoviesTrailer.objects.all()
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

class AddMovie(View):
	""" Store a new movie entry into database."""
