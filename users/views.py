from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import ProfileChangeForm
from connexion.views import messages_langs


@login_required(login_url="/en/users/login")
def profile_view(request, lang=""):
    if request.method == "POST":
        user_form = ProfileChangeForm(request.POST)
        if user_form.is_valid():
            profile = request.user.profile
            profile.platform = user_form.cleaned_data["platform"]
            profile.bio = user_form.cleaned_data["bio"]
            profile.identifiant = user_form.cleaned_data["identifiant"]
            profile.save()
            user = request.user
            user.email = user_form.cleaned_data["email"]
            user.save()
    else:
        user_form = ProfileChangeForm(
            instance=request.user.profile,
            initial={'email': request.user.email})

    should_be_dark = True
    nb_inscrits = User.objects.filter(is_staff=False).count()
    message = messages_langs["make_donation_{}".format(lang)]

    user_prof = request.user

    return render(request, "profil_{}.html".format(lang), locals())


def other_profile_view(request, lang="", username=""):
    should_be_dark = True

    nb_inscrits = User.objects.filter(is_staff=False).count()
    user = get_object_or_404(User, username=username)
    message = messages_langs["make_donation_{}".format(lang)]

    return render(request, "profil_{}.html".format(lang), locals())


def user_list_view(request, lang=""):
    users = User.objects.all()
    should_be_dark = True
    nb_inscrits = User.objects.filter(is_staff=False).count()

    return render(request, "user_list_{}.html".format(lang), locals())
