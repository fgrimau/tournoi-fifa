from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url="/en/users")
def profile_view(request, lang=""):
    should_be_dark = True
    nb_inscrits = User.objects.filter(is_staff=False).count()
    return render(request, "profil_{}.html".format(lang), locals())
