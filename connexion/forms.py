from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password'
        ]
        widgets = {'password': forms.PasswordInput()}


class CompleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user', 'platform', 'identifiant', 'bio',
        ]

        widgets = {'user': forms.HiddenInput()}


class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=150)


class ResetPasswordForm2(forms.Form):
    new_password = forms.CharField(
        max_length=150, widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        max_length=150, widget=forms.PasswordInput())
