from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'cineAthome.views.home', name='home'),
    url(r'^polls/', include('polls.urls')),
    url(r'^lsm/', include('lsm.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
