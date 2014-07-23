from django.shortcuts import render
from games.models import Game

def home_page(request):
    latest_games_list = Game.objects.all()[:5]
    return render(request, 'common/home_page.html', {'latest_games_list': latest_games_list})