from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=150)
    phone = forms.CharField(max_length=150)
    text = forms.CharField(max_length=150)
