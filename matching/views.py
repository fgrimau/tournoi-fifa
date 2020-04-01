from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from matching.models import Poule
from matching.forms import PouleForm
from matching.utils import create_pools
from users.models import Profile
import json


def scoreboard_view(request, lang="", platform=""):
    if platform != "ps4" and platform != "xbox":
        return render(request, "choose_scoreboard.html", locals())

    poules = Poule.objects.filter(platform=platform)
    should_be_dark = True
    nb_inscrits = User.objects.filter(is_staff=False).count()
    return render(request, "scoreboard_{}.html".format(lang), locals())


@staff_member_required
def create_poules_view(request, lang=""):
    if request.method == "POST":
        form = PouleForm(request.POST)
        if form.is_valid():
            preview = True
            xbox_preview = create_pools(
                form.cleaned_data["nb_xbox_poules"], "b")
            ps4_preview = create_pools(
                form.cleaned_data["nb_ps4_poules"], "a")

            json_ps4 = json.dumps(ps4_preview)
            json_xbox = json.dumps(xbox_preview)
    else:
        form = PouleForm()
        preview = False

    should_be_dark = True
    PS4_users = Profile.objects.filter(platform="a", user__is_staff=False)
    XBOX_users = Profile.objects.filter(platform="b", user__is_staff=False)
    nb_inscrits = User.objects.filter(is_staff=False).count()

    return render(request, "create_poules.html", locals())


@staff_member_required
def confirm_pools_view(request, lang=""):
    if request.method != "POST":
        return HttpResponseBadRequest("Mauvaise méthode !")

    form = request.POST

    for poule_nb, usernames in json.loads(form["ps4_pools"]).items():
        pouleObj = Poule(platform="ps4")
        pouleObj.save()
        for username in usernames:
            prof = User.objects.get(username=username).profile
            prof.poule = pouleObj
            prof.save()
    for poule_nb, usernames in json.loads(form["xbox_pools"]).items():
        pouleObj = Poule(platform="xbox")
        pouleObj.save()
        for username in usernames:
            prof = User.objects.get(username=username).profile
            prof.poule = pouleObj
            prof.save()

    return HttpResponseRedirect("/{}/".format(lang))
