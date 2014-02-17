from django.http import Http404
from django.shortcuts import render
from games.models import Game

def index(request):
    latest_games_list = Game.objects.all()[:5]
    return render(request, 'games/index.html', {'latest_games_list': latest_games_list})

def game(request, name):
    try:
        game = Game.objects.get(name=name)
    except:
        game = None
        raise Http404

    if game.platform == game.FLASH:
        return render(request, 'games/flash_game.html', {'game': game})
    elif game.platform == game.UNITY:
        return render(request, 'games/unity_game.html', {'game': game})
    elif game.platform == game.HTML5:
        return render(request, 'games/html5_game.html', {'game': game})
    else:
        raise Http404
