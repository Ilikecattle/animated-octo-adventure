import random

from django.conf import settings
from django.db import models

from caroftheday.models import Car

TOTAL_NUM_OF_CHOICES = 4
NUM_INCORRECT_CHOICES = TOTAL_NUM_OF_CHOICES - 1
HALF_YEAR_RANGE = 10

class Question(models.Model):
    car = models.ForeignKey(Car)
    numCorrect = models.IntegerField(null=True, blank=True)
    numIncorrect = models.IntegerField(null=True, blank=True)

    def get_year_choices(self):
        actual_car_year = self.car.year
        
        year_choices = []
        
        possible_year_choices = range(actual_car_year - HALF_YEAR_RANGE, actual_car_year + HALF_YEAR_RANGE)
        possible_year_choices.remove(actual_car_year)
        
        random.sample(range(HALF_YEAR_RANGE), NUM_INCORRECT_CHOICES)
        
        year_choices.extend(random.sample(possible_year_choices, NUM_INCORRECT_CHOICES))
        year_choices.append(actual_car_year)
        random.shuffle(year_choices)

        return year_choices

    def __unicode__(self):
        return self.car.__unicode__()
