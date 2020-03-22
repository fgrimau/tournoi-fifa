from django.contrib import admin
import matching.models


class HistoryAdmin(admin.ModelAdmin):
    list_display = [
        "id", "winner", "looser", "winner_points",
        "looser_points", "date_played"]
    list_filter = ["winner", "looser", "date_played"]
    ordering = ["date_played"]
    search_fields = ["winner", "looser"]


class PouleAdmin(admin.ModelAdmin):
    list_display = ["id", "platform", "is_finished"]
    list_filter = ["platform", "is_finished"]
    ordering = ["id"]
    search_fields = ["id", "platform"]


admin.site.register(matching.models.Poule, PouleAdmin)
admin.site.register(matching.models.History, HistoryAdmin)
