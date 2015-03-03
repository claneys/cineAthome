from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cineAthome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'polls.views.pollForm_view', name='poll_form'),
    url(r'^create/$', 'polls.views.createPollForm_view', name='create_poll'),
)