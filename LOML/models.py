from django.db import models
from datetime import date

class Message(models.Model):    
    text = models.CharField(max_length=1000)
    date = models.DateField(default=date.today)
    url  = models.URLField(max_length=1000)

    def __unicode__(self):
        return self.text
