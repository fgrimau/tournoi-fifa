from django.urls import path
import matching.views

urlpatterns = [
    path(
        '<slug:platform>/', matching.views.scoreboard_view,
        name="scoreboard_view"),
]
