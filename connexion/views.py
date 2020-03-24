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
    'payment_fr': "Afin de finaliser votre inscription, nous vous demandons de\
    faire un don de minimum <strong>6€</strong> au CHU Saint-Pierre via \
    <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    ce lien</a>, et de \
    nous envoyer un screenshot/une photo par mail à l'adresse \
    <strong>info@fifa-covid19.be</strong>",
    'payment_en': "In order to finalize your registration, we ask you to \
    make a minimum donation of <strong>6€</strong> at CHU Saint-Pierre via \
    <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    this link </a>, and send us a screenshot / photo by email to the address\
    <strong>info@fifa-covid19.be</strong>",
    'payment_nl': "Om uw registratie af te ronden, vragen wij u om \
    een minimale donatie van <strong>6€</strong> te maken bij CHU Saint-Pierre via \
    deze link <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    </a>, en stuur ons een screenshot / foto per e-mail naar het adres \
    <strong>info@fifa-covid19.be</strong>",
    "already_paid_fr": "Vous avez confirmé votre inscription ! Si vous le \
    souhaitez, vous pouvez toujours \
    <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    faire un don supplémentaire</a>",
    "already_paid_en": "You have already confirmed your registration ! if you wish \
    you can always \
    <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
    make an additional donation</a>",
    "already_paid_nl": "U heeft uw inschrijving bevestigd! Indeen gewenst \
    kunt u altijd  \
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
    message = messages_langs["payment_{}".format(lang)]
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
