from django.shortcuts import render


def profile_view(request, lang=""):
    return render(request, "profil.html", locals())
