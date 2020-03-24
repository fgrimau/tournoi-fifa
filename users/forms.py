from django import forms
from users.models import Profile


class ProfileChangeForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = [
            'email', 'platform', 'identifiant', 'bio',
        ]
