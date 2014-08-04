from games.models import Game

def games_list(request):
    return { 'games_list' : Game.objects.all(), }