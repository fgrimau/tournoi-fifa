from django.db import models
from django.contrib.auth.models import User


class Poule(models.Model):
    is_finished = models.BooleanField(default=False)

    choices = (
        ('ps4', 'PS4'),
        ('xbox', 'XBOX'),
    )

    platform = models.CharField(
        max_length=4, choices=choices, verbose_name="platforme", default="ps4")

    @property
    def ranking(self):
        print(sorted(
            list(self.pool_players.all()),
            key=lambda x: x.total_points, reverse=True))
        return sorted(
            list(self.pool_players.all()),
            key=lambda x: x.total_points, reverse=True)


class History(models.Model):
    winner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="winner")
    looser = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="looser")
    winner_points = models.IntegerField(default=0)
    looser_points = models.IntegerField(default=0)

    date_played = models.DateTimeField(auto_now_add=True)

    null_match = models.BooleanField(default=False)
