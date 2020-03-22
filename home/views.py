from django.shortcuts import render


def lang_view(request):
    return render(request, "lang.html")


def home(request, lang=""):
    if lang == "":
        return lang_view(request)

    return render(request, "index_{}.html".format(lang), locals())
