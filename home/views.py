from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from connexion.forms import ResetPasswordForm, ResetPasswordForm2
from connexion.models import Forgotten_pass
from home.forms import ContactForm
import secrets


messages_langs = {
    'mail_subj_reinit_fr': "Réinitialisation du mot de passe FIFA-COVID19",
    'mail_subj_reinit_en': "FIFA-COVID19 password reset",
    'mail_subj_reinit_nl': "FIFA-COVID19-wachtwoord opnieuw instellen",
    'mail_mess_reinit_fr': "Une demande de réinitialisation de votre mot de passe a été faite pour votre compte sur le site fifa-covid19.be\n \
Pour continuer la réinitialisation, veuillez suivre ce lien {}\n \
Si vous n'etes pas à l'origine de cette demande, ou que vous ne possédez pas de compte sur notre site, vous pouvez ignorer ce message",
    'mail_mess_reinit_en': "A request to reset your password was made for your account on the site fifa-covid19.be\n \
To continue resetting, please follow this link {}\n \
If you are not the originator of this request, or if you do not have an account on our site, you can ignore this message",
    'mail_mess_reinit_nl': "Er werd een verzoek ingediend om je wachtwoord opnieuw in te stellen voor je account op de site fifa-covid19.be\n \
Volg deze link om door te gaan met resetten {}\n \
Als u niet de initiator van dit verzoek bent, of als u geen account op onze site heeft, kunt u dit bericht negeren",
    'no_user_fr': "Aucun compte n'a été trouvé avec ce pseudonyme !",
    'no_user_en': "No account was found with these credentials !",
    'no_user_nl': "Geen account gevonden met dit pseudoniem !",
    'email_sent_fr': "Un email a été envoyé à votre adresse {} (Vérifiez dans les spams !)",
    'email_sent_en': "An email has been sent to your address {} (Be sure to check your spams !)",
    'email_sent_nl': "Er is een e-mail verzonden naar uw adres {} (controleer spam !)",
    'not_conc_pass_fr': "Les mots de passe ne correspondent pas !",
    'not_conc_pass_en': "The passwords differ !",
    'not_conc_pass_nl': "De wachtwoorden verschillen !",
    'Not_completed_fr': "Vous n'avez pas fini de compléter votre profil, \
    cliquez <a href='/fr/users/complete/'>ici</a> pour le compléter",
    'Not_completed_en': "Your profile is not completed yet, \
    click <a href='/en/users/complete/'>here</a> to complete it",
    'Not_completed_nl': "Uw profiel is nog niet volledig ingevuld, \
    klik <a href='/en/users/complete/'>hier</a> om het aan te vullen",
}


def lang_view(request):
    return render(request, "lang.html")


def home(request, lang=""):
    if lang == "":
        return lang_view(request)

    nb_inscrits = User.objects.filter(is_staff=False).count()
    if request.user.is_authenticated:
        try:
            print("user.profile =", request.user.profile)
        except:
            messages.add_message(
                request,
                messages.WARNING,
                messages_langs["Not_completed_{}".format(lang)]
            )

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


def contact_team(request, lang=""):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                'Nouveau message via le formulaire de contact',
                "Nouveau message via le formulaire de contact !\n\n\
De : {} ({} - {})\nMessage : {}\n\n\nJosianne secrétaire".format(
                    form.cleaned_data["name"], form.cleaned_data["email"],
                    form.cleaned_data["phone"], form.cleaned_data["text"]),
                "josianne.secretaire@fifa-covid19.be", ["info@fifa-covid19.be",])

    return HttpResponseRedirect("/{}/".format(lang))
