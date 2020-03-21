from django.db import models
from django.contrib.auth.models import User


class History(models.Model):
    winner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="winner")
    looser = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="looser")
    winner_points = models.IntegerField(default=0)
    looser_points = models.IntegerField(default=0)

    date_played = models.DateTimeField(auto_now_add=True)

    null_match = models.BooleanField(default=False)
