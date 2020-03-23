from django.contrib import admin

from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user", "platform", "identifiant",
        "total_points", "poule"]
    list_filter = ["user", "id"]
    ordering = ["id"]
    search_fields = [
        "user", "platform", "identifiant"]

    def total_points(self, profile):
        return profile.total_points


admin.site.register(Profile, ProfileAdmin)
