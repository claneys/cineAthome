# Create your models here.
from django.db import connection, models
from django.utils.translation import ugettext_lazy as _

from poll import CreatedPoll 

class Vote(models.Model):
    idVote = models.AutoField(primary_key=True)
    idPoll = models.ForeignKey(CreatedPoll)
    name  = models.CharField(_(u'Name'), max_length=32)
    movie_1 = models.BooleanField()
    movie_2 = models.BooleanField()
    movie_3 = models.BooleanField()
    movie_4 = models.BooleanField()
    meal_1 = models.BooleanField()
    meal_2 = models.BooleanField()
    
    def __unicode__(self):
        return 'vote on poll %s' % (self.idPoll)
    
    class Meta:
        app_label = 'polls'
        