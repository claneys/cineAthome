from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cineAthome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^(?P<title>.*)\/$', 'lsm.views.movie_details', name='movie_details'),
    url(r'^$', 'lsm.views.list_movie', name='list_movie')
)