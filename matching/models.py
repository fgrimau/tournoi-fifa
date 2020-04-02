from django.db import models
from django.utils import timezone
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
        return sorted(
            list(self.pool_players.all()),
            key=lambda x: x.total_points, reverse=True)


class Finale_poule(models.Model):
    level = models.CharField(default="", max_length=20)

    player1 = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name="as_finale_player1")
    player2 = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name="as_finale_player2")

    finished = models.BooleanField(default=False)
    winner = models.IntegerField(default=0, verbose_name="winner nb")

    choices = (
        ('ps4', 'PS4'),
        ('xbox', 'XBOX'),
    )

    platform = models.CharField(
        max_length=4, choices=choices, verbose_name="platforme", default="ps4")

    @property
    def winner_user(self):
        if self.winner == 0:
            return None
        elif self.winner == 1:
            return self.player1
        else:
            return self.player2


class History(models.Model):
    player1 = models.ForeignKey(
        User, null=True, on_delete=models.PROTECT, related_name="as_player1")
    player2 = models.ForeignKey(
        User, null=True, on_delete=models.PROTECT, related_name="as_player2")
    player1_points = models.IntegerField(default=0)
    player2_points = models.IntegerField(default=0)

    played = models.BooleanField(default=False)
    date_played = models.DateTimeField(default=timezone.now)

    null_match = models.BooleanField(default=False)

    @property
    def winner_pseudo(self):
        if self.player1_points > self.player2_points:
            return self.player1.username
        elif self.player2_points > self.player1_points:
            return self.player2.username
        else:
            return "none"

    @property
    def winner_points(self):
        if self.player1_points > self.player2_points:
            return self.player1_points
        elif self.player2_points > self.player1_points:
            return self.player2_points

    @property
    def looser_points(self):
        if self.player1_points > self.player2_points:
            return self.player1_points
        elif self.player2_points > self.player1_points:
            return self.player2_points
