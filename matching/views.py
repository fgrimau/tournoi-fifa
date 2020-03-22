from django.shortcuts import render

from matching.models import Poule


def scoreboard_view(request, lang="", platform=""):
    if platform != "ps4" and platform != "xbox":
        return render(request, "choose_scoreboard.html", locals())

    poules = Poule.objects.filter(platform=platform)
    return render(request, "scoreboard.html", locals())
