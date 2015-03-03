# Create your models here.
from django.db import connection, models
from django.utils.translation import ugettext_lazy as _
import re

class movieManager(models.Manager):    
    def get_movie_by_id(self, idMovie):
        def runtime(seconde):
            heure = seconde /3600
            seconde %= 3600
            minute = seconde/60
            return "%dh%d" % (heure,minute)
        
        def get_thumbnail(c08):
            return re.sub(r'^.*preview="(.*)">.*$', r'\1', c08)
        
        idMovie = int(idMovie)
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT idMovie, c00, c01, c05, c07, c08, c11, c14, c21
            FROM MyVideos78.movie
            WHERE idMovie = %s
            GROUP BY c00""", idMovie)
        
        movie = [{'idMovie': row[0],
            'title': row[1],
            'synopsis': row[2],
            'rating': row[3],
            'year': row[4],
            'thumbnail': get_thumbnail(row[5]),
            'runtime': runtime(int(row[6])),
            'genre': row[7],
            'country': row[8]} for row in cursor.fetchall()]
        
        movie = movie[0]
            
        return movie
    
    def get_movie_by_title(self, title):
        def runtime(seconde):
            heure = seconde /3600
            seconde %= 3600
            minute = seconde/60
            return "%dh%d" % (heure,minute)
        
        def get_thumbnail(c08):
            return re.sub(r'^.*preview="(.*)">.*$', r'\1', c08)
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT idMovie, c00, c01, c05, c07, c08, c11, c14, c21
            FROM MyVideos78.movie
            WHERE c00 = %s
            GROUP BY c00""", title)
        
        movie = [{'idMovie': row[0],
            'title': row[1],
            'synopsis': row[2],
            'rating': row[3],
            'year': row[4],
            'thumbnail': get_thumbnail(row[5]),
            'runtime': runtime(int(row[6])),
            'genre': row[7],
            'country': row[8]} for row in cursor.fetchall()]
        
        movie = movie[0]
        
        return movie
    
    # Return an iterable list of boolean tuple usable in Django ChoiceField
    def get_all_movies_choices(self):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT idMovie, c00
            FROM MyVideos78.movie
            GROUP BY c00""")
        movies = [ (row[0], row[1]) for row in cursor.fetchall()]
        
        return movies

    def get_all_movies(self):
            cursor = connection.cursor()
            cursor.execute("""
                SELECT c00, c07, c14
                FROM MyVideos78.movie
                GROUP BY c00""")
            movies = [ (row[0], row[1], row[2]) for row in cursor.fetchall()]
                
            return movies

class movie(models.Model):
    objects = movieManager()
    
    def __unicode__(self, idMovie):
        return self.objects.get_movie_by_id(idMovie)[0]['title']
    
    class Meta:
        app_label = "lsm"
        
        