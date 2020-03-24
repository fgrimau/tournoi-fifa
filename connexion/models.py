from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Forgotten_pass(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    reinitialized = models.BooleanField(default=False)
    link_key = models.CharField(
        null=True, blank=True, default="", max_length=40)

    @property
    def link_active(self):
        return timezone.now() - self.date_created < timezone.timedelta(
            hours=24) and not self.reinitialized
