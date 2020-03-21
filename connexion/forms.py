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
            'psn_profile', 'xboxlive_profile', 'origin_profile',
        ]
