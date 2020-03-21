from django.shortcuts import render, redirect
from connexion.forms import UserForm, CompleteProfileForm


def register_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            form.save()
            return redirect("/")
    else:
        form = UserForm
    return render(request, "register.html", locals())


def complete_profile_view(request):
    if request.method == "POST":
        form = CompleteProfileForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            form.save()
            return redirect("/")
    else:
        form = CompleteProfileForm
    return render(request, "register.html", locals())



def login_view(request):
    return render(request, "login.html")
