import hashlib
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q, F

from matching.models import Poule


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    choices = (
        ('a', 'PS4'),
        ('b', 'XBOX'),
    )

    identifiant = models.CharField(
        max_length=150, verbose_name="platform username")
    platform = models.CharField(
        max_length=1, default="a", choices=choices,
        verbose_name="Player's platform")
    bio = models.TextField()
    poule = models.ForeignKey(
        Poule, on_delete=models.SET_NULL,
        related_name="pool_players", default=None,
        null=True, blank=True)

    @property
    def gravatar(self):
        mail = self.user.email.lower().encode('utf8')
        return "//www.gravatar.com/avatar/{}?s=500".format(
            hashlib.md5(mail).hexdigest())

    @property
    def total_points(self):
        total = self.total_victories * 3
        total += self.total_null
        return total

    @property
    def total_victories(self):
        return (
            self.user.as_player1.filter(
                null_match=False,
                player1_points__gt=F('player2_points'),
                played=True
            ) | self.user.as_player2.filter(
                null_match=False,
                player2_points__gt=F('player1_points'),
                played=True
            )).count()

    @property
    def total_goals(self):
        total = 0
        qs = self.user.as_player1.all()
        qs_win = qs.filter(
            null_match=False,
            player1_points__gt=F('player2_points'),
            played=True
        )
        qs_loos = qs.filter(
            null_match=False,
            player1_points__lt=F('player2_points'),
            played=True
        )
        for history in qs_win | qs_loos:
            total += history.player1_points

        qs = self.user.as_player2.all()
        qs_win = qs.filter(
            null_match=False,
            player2_points__gt=F('player1_points'),
            played=True
        )
        qs_loos = qs.filter(
            null_match=False,
            player2_points__lt=F('player1_points'),
            played=True
        )
        for history in qs_win | qs_loos:
            total += history.player2_points

        return total

    @property
    def total_got_goals(self):
        total = 0
        qs = self.user.as_player1.all()
        qs_win = qs.filter(
            null_match=False,
            player1_points__gt=F('player2_points'),
            played=True
        )
        qs_loos = qs.filter(
            null_match=False,
            player1_points__lt=F('player2_points'),
            played=True
        )
        for history in qs_win | qs_loos:
            total += history.player2_points

        qs = self.user.as_player2.all()
        qs_win = qs.filter(
            null_match=False,
            player2_points__gt=F('player1_points'),
            played=True
        )
        qs_loos = qs.filter(
            null_match=False,
            player2_points__lt=F('player1_points'),
            played=True
        )
        for history in qs_win | qs_loos:
            total += history.player1_points

        return total

    @property
    def total_null(self):
        return (
            self.user.as_player1.all() | self.user.as_player2.all()).filter(
                null_match=True,
                played=True
            ).count()

    @property
    def total_defeats(self):
        return (
            self.user.as_player1.filter(
                null_match=False,
                player2_points__gt=F('player1_points'),
                played=True
            ) | self.user.as_player2.filter(
                null_match=False,
                player1_points__gt=F('player2_points'),
                played=True
            )).count()

    @property
    def history(self):
        return (
            self.user.as_player1.all() | self.user.as_player2.all()).filter(
                played=True
            ).order_by("-date_played")

    @property
    def to_come(self):
        return (
            self.user.as_player1.all() | self.user.as_player2.all()).filter(
                played=False
            ).order_by("date_played")

    @property
    def get_diff(self):
        return self.total_goals - self.total_got_goals
