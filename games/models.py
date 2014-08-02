from django.db import models
from django.contrib.sites.models import Site

class Category(models.Model):
    class Meta():
        verbose_name_plural = "categories"
    name = models.CharField(max_length=100)
    games = models.ManyToManyField('Game', blank=True)
    
    def __unicode__(self):
        return self.name

class Game(models.Model):
    FLASH = 'Flash'
    UNITY = 'Unity'
    HTML5 = 'Html5'
    TYPE_CHOICES = (
        (FLASH, 'Flash'),
        (UNITY, 'Unity'),
        (HTML5, 'Html5'),
    )
    
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=5, choices=TYPE_CHOICES)
    description = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    categories = models.ManyToManyField(Category, through=Category.games.through, blank=True)
    thumbnail = models.CharField(max_length=100, blank=True)
    sites = models.ManyToManyField(Site)
    
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('games.views.game', args=[self.name])

    def __unicode__(self):
        return self.name
