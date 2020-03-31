from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse

from connexion.forms import UserForm, CompleteProfileForm


messages_langs = {
    'wlcbck_fr': "Rebonjour {} !",
    'wlcbck_en': "Welcome back {} !",
    'wlcbck_nl': "Welkom terug{} !",
    'faillogin_fr': "Vos identifiants ne correspondent à aucun compte !",
    'faillogin_en': "These login does not correspond to any account !",
    'faillogin_nl': "Uw identificatiegegevens komen met geen enkel account overeen!",
    'disco_fr': "Vous avez été déconnecté",
    'disco_en': "You've been disconnected",
    'disco_nl': "Je bent verbroken",

    "make_donation_fr": "Les hopitaux ont besoin de vous ! \
    <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    faire un don supplémentaire</a>",

    "make_donation_en": "the hospitals need you ! \
    <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    make an additional donation</a>",

    "make_donation_nl": "ziekenhuizen hebben u nodig ! \
    <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    een extra donatie doen</a>",

    "understood_fr": "Compris !",
    "understood_en": "Understood !",
    "understood_nl": "Begrepen !",
}


def register_view(request, lang=""):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            user = form.save()
            user.set_password(form.cleaned_data["password"])
            user.save()
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"])
            login(request, user)
            return redirect(
                reverse("complete_registration", kwargs={'lang': lang}))
    else:
        form = UserForm

    title = "Register"
    return render(request, "register.html", locals())


def complete_profile_view(request, lang=""):
    if request.method == "POST":
        form = CompleteProfileForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            profile = form.save()
            profile.user = request.user
            profile.save()
            return redirect(
                reverse("final_registration", kwargs={'lang': lang}))
    else:
        form = CompleteProfileForm(initial={'user': request.user})
        title = "Register"
    return render(request, "register.html", locals())


def payment_view(request, lang=""):
    message = messages_langs["make_donation_{}".format(lang)]
    understood = messages_langs["understood_{}".format(lang)]
    return render(request, "payment.html", locals())


def login_view(request, lang=""):
    if request.method != "POST":
        return render(request, 'login.html', locals())

    form = request.POST
    username = form["username"]
    password = form["password"]

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(
            request, messages.SUCCESS,
            messages_langs['wlcbck_{}'.format(lang)].format(user.username))
        return HttpResponseRedirect("/{}/".format(lang))
    else:
        messages.add_message(
            request, messages.ERROR,
            messages_langs["faillogin_{}".format(lang)])
        return HttpResponseRedirect("/{}/users/login/".format(lang))


def disconnect(request, lang=""):
    logout(request)

    messages.add_message(
        request, messages.WARNING,
        messages_langs["disco_{}".format(lang)])

    return HttpResponseRedirect("/{}/".format(lang))
