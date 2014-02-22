from django.contrib import admin
from models import Game, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
