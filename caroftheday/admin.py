from django.contrib import admin
from models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('date',)

admin.site.register(Car, CarAdmin)
