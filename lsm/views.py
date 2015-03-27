from django.shortcuts import render
from django.shortcuts import render_to_response
from models import movie as m
import re
from urllib import quote

# Create your views here.
def list_movie(request):
    movies = m.objects.get_all_movies()
    return render_to_response('lsm/lsm.html', { 'movies' : movies })
    
def movie_details(request, title):
    movie = m.objects.get_movie_by_title(title)
    return render_to_response('lsm/movie_details.html', {'movie' : movie })
    