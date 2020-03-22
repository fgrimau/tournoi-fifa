from django.contrib.auth.models import User
from django.db import models

from matching.models import Poule


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    psn_profile = models.CharField(
        max_length=150, default="none provided", verbose_name="Pseudo PSN")
    xboxlive_profile = models.CharField(
        max_length=150, default="none provided",
        verbose_name="Pseudo XBoxLive")
    origin_profile = models.CharField(
        max_length=150, default="none provided", verbose_name="Pseudo Origin")

    poule = models.ForeignKey(
        Poule, on_delete=models.PROTECT,
        related_name="pool_players", default=None)

    @property
    def total_points(self):
        return self.user.winner.filter(null_match=False).count() * 3\
            + self.user.winner.filter(null_match=True).count()

    @property
    def total_victories(self):
        return self.user.winner.filter(null_match=False).count()

    @property
    def total_null(self):
        return (self.user.winner.filter(null_match=True) | self.user.looser.filter(null_match=True)).count()

    @property
    def total_defeats(self):
        return self.user.looser.filter(null_match=False).count()

    @property
    def history(self):
        return self.winner.all() | self.looser.all()
