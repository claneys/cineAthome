# Create your models here.
from django.db import connection, models
from django.utils.translation import ugettext_lazy as _

class CreatePoll(models.Model):
    idPoll = models.AutoField(primary_key=True)
    movie_1 = models.CharField(max_length=50)
    movie_2 = models.CharField(max_length=50)
    movie_3 = models.CharField(max_length=50)
    movie_4 = models.CharField(max_length=50)
    meal_1 = models.CharField(max_length=50)
    meal_2 = models.CharField(max_length=50)

    def __unicode__(self):
        return "Poll #%s" % str(self.idPoll)
                   
    class Meta:
        app_label = 'polls'