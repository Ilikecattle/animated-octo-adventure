from django.db import models
from datetime import date

class Message(models.Model):    
    text = models.CharField(max_length=1000)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.text
