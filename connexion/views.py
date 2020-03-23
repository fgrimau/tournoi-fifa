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
            return redirect("/")
    else:
        form = CompleteProfileForm(initial={'user': request.user})
    return render(request, "register.html", locals())


def login_view(request, lang=""):
    if request.method != "POST":
        return render(request, 'login.html', locals())

    form = request.POST
    username = form["username"]
    password = form["password"]

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/{}/".format(lang))
    else:
        print("noKay")
        messages.add_message(
            request, messages.ERROR,
            "Vos identifiants ne correspondent à \
            aucun compte !")
        return HttpResponseRedirect("/{}/users/login/".format(lang))


def disconnect(request, lang=""):
    logout(request)

    messages.add_message(
        request, messages.WARNING,
        "Vous avez été déconnecté")
    return HttpResponseRedirect("/{}/".format(lang))
