from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from connexion.forms import UserForm, CompleteProfileForm
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def register_view(request, lang=""):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            form.save()
            return redirect("/")
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
    else:
        form = request.POST
        username = form["username"]
        password = form["password"]

        print("foferofreofjre :", username)

        try:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS,
                    "Rebonjour {}".format(request.user.first_name))
                print("Kay")
                return HttpResponseRedirect("/{}/".format(lang))
            else:
                print("noKay")
                messages.add_message(
                    request, messages.ERROR,
                    "Vos identifiants ne correspondent à \
                    aucun compte !")
                return HttpResponseRedirect("/{}/".format(lang))
        except Exception as e:
            print("Error : ", e)

            messages.add_message(
                request, messages.ERROR,
                "Vos identifiants ne correspondent à \
                aucun compte !")
        return HttpResponseRedirect("/{}/".format(lang))


def disconnect(request, lang=""):
    logout(request)

    messages.add_message(
        request, messages.WARNING,
        "Vous avez été déconnecté")
    return HttpResponseRedirect("/{}/".format(lang))
