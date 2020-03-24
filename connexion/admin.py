from django.contrib import admin

from connexion.models import Forgotten_pass


class ResetPasswordAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user", "date_created", "link_active"]
    list_filter = ["user", "id", "date_created"]
    ordering = ["id"]
    search_fields = ["id", "user"]

    def link_active(self, forgotten):
        return forgotten.link_active


admin.site.register(Forgotten_pass, ResetPasswordAdmin)
