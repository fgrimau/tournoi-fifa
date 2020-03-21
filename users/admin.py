from django.contrib import admin
import users.models


class HistoryAdmin(admin.ModelAdmin):
    list_display = ["player_1", "player_2", "score_player_1", "score_player_2"]
    list_filter = ["player_1", "player_2", "date_played"]
    ordering = ["date_played"]
    search_fields = ["player_1", "player_2"]


admin.site.register(users.models.History, HistoryAdmin)
