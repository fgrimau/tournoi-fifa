from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from connexion.forms import UserForm, CompleteProfileForm
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.urls import reverse


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
    return render(request, "register.html", locals())


def payment_view(request, lang=""):
    message = "Afin de finaliser votre inscription, nous vous demandons de \
        faire un don de minimum <strong>6€</strong> au CHU Saint-Pierre via \
        <a href='https://donate.kbs-frb.be/Brussel_UMC_SintPieter/~mon-don?_cv=1'>\
        ce lien</a>, et de \
        nous envoyer un screenshot/une photo par mail à l'adresse \
        <strong>info@fifa-covid19.be</strong>"
    understood = "Compris !"
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
        if lang == "fr":
            messages.add_message(
                request, messages.SUCCESS,
                "Rebonjour {} !".format(user.username))
        if lang == "nl":
            messages.add_message(
                request, messages.SUCCESS,
                "Welcome back {} !".format(user.username))
        if lang == "en":
            messages.add_message(
                request, messages.SUCCESS,
                "Welcome back {} !".format(user.username))
        return HttpResponseRedirect("/{}/".format(lang))
    else:
        if lang == "fr":
            messages.add_message(
                request, messages.ERROR,
                "Vos identifiants ne correspondent à aucun compte !")
        if lang == "nl":
            messages.add_message(
                request, messages.ERROR,
                "These login does not correspond to any account !")
        if lang == "en":
            messages.add_message(
                request, messages.ERROR,
                "These login does not correspond to any account !")
        return HttpResponseRedirect("/{}/users/login/".format(lang))


def disconnect(request, lang=""):
    logout(request)

    if lang == "fr":
        messages.add_message(
            request, messages.WARNING,
            "Vous avez été déconnecté")
    if lang == "nl":
        messages.add_message(
            request, messages.WARNING,
            "You've been disconnected")
    if lang == "en":
        messages.add_message(
            request, messages.WARNING,
            "You've been disconnected")

    return HttpResponseRedirect("/{}/".format(lang))
