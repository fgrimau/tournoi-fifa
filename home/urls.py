from django.urls import path
import home.views

urlpatterns = [
    path('', home.views.home, name="home_view"),
    path('scores', home.views.scoreboard_view, name="scoreboard_view"),
]
