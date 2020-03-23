from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from connexion.forms import UserForm, CompleteProfileForm
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login


def register_view(request, lang=""):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            user = form.save()
            return redirect("/{}".format(lang))
    else:
        form = UserForm
    return render(request, "register.html", locals())


def complete_profile_view(request, lang=""):
    if request.method == "POST":
        form = CompleteProfileForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            form.save()
            return redirect("/")
    else:
        form = CompleteProfileForm
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
