import datetime

from django.test import TestCase
from carquizgame.models import Question
from caroftheday.models import Car

class QuestionTestCase(TestCase):
    def setUp(self):
        car = Car.objects.create(
            imageLink="",
            link="",
            description="Adam's first car",
            image="",
            year="1978",
            make="Honda",
            model="Civic",
            date=datetime.datetime.today()
            )
        Question.objects.create(car=car)
    
    def test_question(self):
        """Test the creation of a question"""
        question = Question.objects.get(car=Car.objects.all()[0])
        self.assertIsNotNone(question)
        self.assertIsNone(question)
