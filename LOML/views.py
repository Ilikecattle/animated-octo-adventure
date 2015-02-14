import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponse
from django.shortcuts import render
from datetime import date

from LOML.models import Message

def message(request):
    try:
        message = Message.objects.get(date=date.today)
    except:
        raise Http404

    return HttpResponse(message.text)

def messages(request):
    try:
        messages = Message.objects.all().values_list('date', 'text', 'url')
    except:
        raise Http404

    messages_json = json.dumps(list(messages), cls=DjangoJSONEncoder)

    return HttpResponse(messages_json, content_type="application/json")

def url(request):
    try:
        message = Message.objects.get(date=date.today)
    except:
        raise Http404

    return HttpResponse(message.url)