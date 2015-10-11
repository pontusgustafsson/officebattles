from django.contrib import admin

# Register your models here.
from .models import Game

class GameAdmin(admin.ModelAdmin):
    fields = ['company', 'office', 'name', 'mode', 'min_players', 'max_players']
    list_display = ('name', 'mode', 'office', 'company', 'created', 'updated')
    list_filter = ['mode', 'created', 'updated']
    search_fields = ['name']

admin.site.register(Game, GameAdmin)
