from django.shortcuts import render


def lang_view(request):
    return render(request, "lang.html")


def home(request, lang=""):
    if lang == "":
        return lang_view(request)

    return render(request, "index.html", locals())


def scoreboard_view(request, lang=""):
    return render(request, "scoreboard.html", locals())
