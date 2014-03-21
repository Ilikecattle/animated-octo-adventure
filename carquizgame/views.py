import random
import json

from datetime import date
from datetime import datetime
from models import Question
from caroftheday.models import Car
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    random_id = random.randint(0, Car.objects.count() - 1)
    car = Car.objects.all()[random_id]
    return render_question_for_car(request, car)

def render_question_for_car(request, car):
    question = Question.objects.get_or_create(car=car)[0]
    return render(request,
        'carquizgame/question.html',
        {
            'question' : question,
            'car' : car,
            'year_options' : question.get_year_choices(),
            'correct_response' : car.year
        }
    )

def question(request, year, month, day):
    dt = date(int(year), int(month), int(day))
    car = get_object_or_404(Car, date=dt)
    return render_question_for_car(request, car)

def check_year(request):
    date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
    guess = request.GET.get('guess')
    car = get_object_or_404(Car, date=date)
    
    if car.year == int(guess):
        json_data = json.dumps({"success":1})
    else:
        json_data = json.dumps({"success":0})
        
    return HttpResponse(json_data, mimetype="application/json")
