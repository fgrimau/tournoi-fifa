from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import ProfileChangeForm
from connexion.views import messages_langs


@login_required(login_url="/en/users")
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
    if request.user.profile.paid:
        message = messages_langs["already_paid_{}".format(lang)]
    else:
        message = messages_langs["payment_{}".format(lang)]

    return render(request, "profil_{}.html".format(lang), locals())
