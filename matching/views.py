from django.shortcuts import render
from django.contrib.auth.models import User

from matching.models import Poule


def scoreboard_view(request, lang="", platform=""):
    if platform != "ps4" and platform != "xbox":
        return render(request, "choose_scoreboard.html", locals())

    poules = Poule.objects.filter(platform=platform)
    should_be_dark = True
    nb_inscrits = User.objects.filter(is_staff=False).count()
    return render(request, "scoreboard_{}.html".format(lang), locals())
