from django.urls import path
import matching.views

urlpatterns = [
    path(
        'create_poules/',
        matching.views.create_poules_view, name="create_poules"),
    path(
        'create_poules/confirm/',
        matching.views.confirm_pools_view, name="confirm_pools"),
    path(
        '<slug:platform>/',
        matching.views.scoreboard_view, name="scoreboard_view"),
]
