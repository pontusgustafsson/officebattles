from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    fields = ['office', 'name', 'mode', 'min_players', 'max_players', 'has_coin_toss']
    list_display = ('name', 'mode', 'office', 'created', 'updated')
    list_filter = ['mode', 'created', 'updated']
    search_fields = ['name']


admin.site.register(Game, GameAdmin)
