from django.http import HttpResponse
from datetime import date

from LOML.models import Message

def message(request):
    
    try:
        message = Message.objects.get(date=date.today)
    except:
        raise Http404

    return HttpResponse(message.text)