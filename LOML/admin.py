from django.contrib import admin
from models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text','date')

admin.site.register(Message, MessageAdmin)
