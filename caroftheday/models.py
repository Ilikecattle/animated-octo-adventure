from django.conf import settings
from django.db import models

class Car(models.Model):
    imageLink = models.FilePathField(path=settings.MEDIA_ROOT)
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='caroftheday')
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.model
