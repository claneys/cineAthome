# Create your models here.
from django.db import connection, models
from django.utils.translation import ugettext_lazy as _

class CreatedPoll(models.Model):
    idPoll = models.AutoField(primary_key=True)
    movie_1 = models.PositiveIntegerField()
    movie_2 = models.PositiveIntegerField()
    movie_3 = models.PositiveIntegerField()
    movie_4 = models.PositiveIntegerField()
    meal_1 = models.URLField(max_length=500)
    meal_2 = models.URLField(max_length=500)

    def __unicode__(self):
        return "Poll #%s" % str(self.idPoll)
                   
    class Meta:
        app_label = 'polls'
        
