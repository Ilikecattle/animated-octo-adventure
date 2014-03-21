from django.conf import settings
from django.db import models

class Car(models.Model):
    imageLink = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    date = models.DateField()
    
    def get_date_string(self):
        return self.date.strftime('%Y-%m-%d')
    
    def get_description(self):
        return str(self.year) + " " + str(self.make) + " " + str(self.model);
    
    def __unicode__(self):
        return self.model
