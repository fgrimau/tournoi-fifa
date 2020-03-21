from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    psn_profile = models.CharField(
        max_length=150, default="none provided", verbose_name="Pseudo PSN")
    xboxlive_profile = models.CharField(
        max_length=150, default="none provided",
        verbose_name="Pseudo XBoxLive")
    origin_profile = models.CharField(
        max_length=150, default="none provided", verbose_name="Pseudo Origin")


class History(models.Model):
    player_1 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="player_1")
    player_2 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="player_2")
    score_player_1 = models.IntegerField(default=0)
    score_player_2 = models.IntegerField(default=0)
    date_played = models.DateTimeField(auto_now_add=True)
