from django.contrib.auth.models import User

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
