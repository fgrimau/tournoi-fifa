from django import forms


class PouleForm(forms.Form):
    nb_ps4_poules = forms.IntegerField(
        label="Nombre de poules pour joueurs PS4")
    nb_xbox_poules = forms.IntegerField(
        label="Nombre de poules pour joueurs XBOX")
