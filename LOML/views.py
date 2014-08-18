from django.http import Http404
from django.shortcuts import render
from datetime import date

from LOML.models import Message

def message(request):
    try:
        message = Message.objects.get(date=date.today)
    except:
        raise Http404

    return render(request, 'LOML/message.html', {'message': message})