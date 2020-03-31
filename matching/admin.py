from django.contrib import admin
import matching.models


class HistoryAdmin(admin.ModelAdmin):
    list_display = [
        "id", "player1", "player2", "player1_points",
        "player2_points", "date_played"]
    list_filter = ["player1", "player2", "date_played"]
    ordering = ["date_played"]
    search_fields = ["player1", "player2"]


class PouleAdmin(admin.ModelAdmin):
    list_display = ["id", "platform", "is_finished"]
    list_filter = ["platform", "is_finished"]
    ordering = ["id"]
    search_fields = ["id", "platform"]


admin.site.register(matching.models.Poule, PouleAdmin)
admin.site.register(matching.models.History, HistoryAdmin)
