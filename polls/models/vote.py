# Create your models here.
from django.db import connection, models
from django.utils.translation import ugettext_lazy as _

class Vote(models.Model):
    name = models.CharField(_(u'Name'),max_length=32)
    idMovie = models.PositiveIntegerField()
    urlDinner = models.URLField(_(u'urlDinner'))
    
    def __unicode__(self):
        return '%s voted for %s and %s' % (self.name, self.idMovie, self.urlDinner)
    
    class Meta:
        app_label = 'Vote'