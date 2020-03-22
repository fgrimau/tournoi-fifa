from django.contrib import admin

from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user", "psn_profile", "xboxlive_profile",
        "origin_profile", "total_points", "poule"]
    list_filter = ["user", "id"]
    ordering = ["id"]
    search_fields = [
        "user", "psn_profile", "xboxlive_profile", "origin_profile"]

    def total_points(self, profile):
        return profile.total_points


admin.site.register(Profile, ProfileAdmin)
