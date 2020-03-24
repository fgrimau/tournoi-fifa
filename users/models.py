import hashlib
from django.contrib.auth.models import User
from django.db import models

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
        verbose_name="Platforme du joueur")
    bio = models.TextField()
    poule = models.ForeignKey(
        Poule, on_delete=models.PROTECT,
        related_name="pool_players", default=None,
        null=True, blank=True)

    paid = models.BooleanField(default=False)

    @property
    def gravatar(self):
        mail = self.user.email.lower().encode('utf8')
        return "//www.gravatar.com/avatar/{}?s=500".format(
            hashlib.md5(mail).hexdigest())

    @property
    def total_points(self):
        return self.user.winner.filter(null_match=False).count() * 3\
            + self.user.winner.filter(null_match=True).count()

    @property
    def total_victories(self):
        return self.user.winner.filter(null_match=False).count()

    @property
    def total_goals(self):
        total = 0
        for history in self.user.winner.all():
            total += history.winner_points
        for history in self.user.looser.all():
            total += history.looser_points
        return total

    @property
    def total_got_goals(self):
        total = 0
        for history in self.user.winner.all():
            total += history.looser_points
        for history in self.user.looser.all():
            total += history.winner_points
        return total

    @property
    def total_null(self):
        return (self.user.winner.filter(null_match=True) | self.user.looser.filter(null_match=True)).count()

    @property
    def total_defeats(self):
        return self.user.looser.filter(null_match=False).count()

    @property
    def history(self):
        return self.user.winner.all() | self.user.looser.all()
