from django.shortcuts import render

from matching.models import Poule


def scoreboard_view(request, lang="", platform=""):
    if platform != "ps4" and platform != "xbox":
        return render(request, "choose_scoreboard.html", locals())

    poules = Poule.objects.filter(platform=platform)
    should_be_dark = True
    return render(request, "scoreboard_{}.html".format(lang), locals())
