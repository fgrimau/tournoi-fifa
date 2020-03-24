from django.shortcuts import render
from django.contrib.auth.models import User


def lang_view(request):
    return render(request, "lang.html")


def home(request, lang=""):
    if lang == "":
        return lang_view(request)

    nb_inscrits = User.objects.filter(is_staff=False).count()

    return render(request, "index_{}.html".format(lang), locals())
