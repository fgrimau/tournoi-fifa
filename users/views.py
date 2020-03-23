from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/en/users")
def profile_view(request, lang=""):
    return render(request, "profil_{}.html".format(lang), locals())
