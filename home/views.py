from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from connexion.forms import ResetPasswordForm, ResetPasswordForm2
from connexion.models import Forgotten_pass
from django.urls import reverse
import secrets


messages_langs = {
    'mail_subj_reinit_fr': "Réinitialisation du mot de passe FIFA-COVID19",
    'mail_subj_reinit_en': "Réinitialisation du mot de passe FIFA-COVID19",
    'mail_subj_reinit_nl': "Réinitialisation du mot de passe FIFA-COVID19",
    'mail_mess_reinit_fr': "Une demande de réinitialisation de votre mot de passe a été faite pour votre compte sur le site fifa-covid19.be\n \
Pour continuer la réinitialisation, veuillez suivre ce lien {}\n \
Si vous n'etes pas à l'origine de cette demande, ou que vous ne possédez pas de compte sur notre site, vous pouvez ignorer ce message",
    'mail_mess_reinit_en': "Une demande de réinitialisation de votre mot de passe a été faite pour votre compte sur le site fifa-covid19.be\n \
Pour continuer la réinitialisation, veuillez suivre ce lien {}\n \
Si vous n'etes pas à l'origine de cette demande, ou que vous ne possédez pas de compte sur notre site, vous pouvez ignorer ce message",
    'mail_mess_reinit_nl': "Une demande de réinitialisation de votre mot de passe a été faite pour votre compte sur le site fifa-covid19.be\n \
Pour continuer la réinitialisation, veuillez suivre ce lien {}\n \
Si vous n'etes pas à l'origine de cette demande, ou que vous ne possédez pas de compte sur notre site, vous pouvez ignorer ce message",
    'no_user_fr': "Aucun compte n'a été trouvé avec ce pseudonyme !",
    'no_user_en': "No account was found with these credentials !",
    'no_user_nl': "No account was found with these credentials !",
    'email_sent_fr': "Un email a été envoyé à votre adresse {} (Vérifiez dans les spams !)",
    'email_sent_en': "An email has been sent to your address {} (Be sure to check your spams !)",
    'email_sent_nl': "An email has been sent to your address {} (Be sure to check your spams !)",
    'not_conc_pass_fr': "Les mots de passe ne correspondent pas !",
    'not_conc_pass_en': "The passwords differ !",
    'not_conc_pass_nl': "The passwords differ !",
}


def lang_view(request):
    return render(request, "lang.html")


def home(request, lang=""):
    if lang == "":
        return lang_view(request)

    nb_inscrits = User.objects.filter(is_staff=False).count()

    return render(request, "index_{}.html".format(lang), locals())


def reset_password(request, lang=""):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():  # Verify the data of the form
            usr = User.objects.filter(username=form.cleaned_data["username"])
            if len(usr) != 1:
                messages.add_message(
                    request, messages.ERROR,
                    messages_langs['no_user_{}'.format(lang)])
                return redirect(
                    reverse("forgotpass", kwargs={'lang': lang})
                )
            passmod = Forgotten_pass()
            passmod.user = usr[0]
            passmod.link_key = secrets.token_hex(20)
            passmod.save()

            send_mail(
                messages_langs['mail_subj_reinit_{}'.format(lang)],
                messages_langs[
                    'mail_mess_reinit_{}'.format(lang)
                ].format("https://fifa-covid19.be/{}/reset/{}".format(
                    lang, passmod.link_key)
                ),
                'info@fifa-covid19.be',
                [usr[0].email],
                fail_silently=False,
            )

            messages.add_message(
                request, messages.WARNING,
                messages_langs[
                    "email_sent_{}".format(lang)
                ].format("{}*****@{}").format(
                    usr[0].email[0], usr[0].email.split("@")[1])
                )

            return HttpResponseRedirect("/{}/".format(lang))
    else:
        form = ResetPasswordForm
        title = "Reset Password"
    return render(request, "register.html", locals())


def reset_password_form_view(request, lang="", token=""):
    passmod = get_object_or_404(
        Forgotten_pass, link_key=token, reinitialized=False)

    if request.method == "POST":
        form = ResetPasswordForm2(request.POST)
        if form.is_valid():  # Verify the data of the form
            if form.cleaned_data["new_password"] != form.cleaned_data["confirm_password"]:
                messages.add_message(
                    request, messages.ERROR,
                    messages_langs["not_conc_pass_{}".format(lang)])
                form = ResetPasswordForm2
                title = "Reset Password"
                return render(request, "register.html", locals())
            passmod.reinitialized = True
            passmod.save()
            user = passmod.user
            user.set_password(form.cleaned_data["new_password"])
            user.save()
            return HttpResponseRedirect("/{}/".format(lang))
    else:
        form = ResetPasswordForm2
        title = "Reset Password"
    return render(request, "register.html", locals())
