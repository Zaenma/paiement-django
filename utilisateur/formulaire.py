from django import forms
from .models import Utilisateur


class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        # fields = ('age', 'titre', 'nom', 'prenom', 'telephone', 'email')
        fields = "__all__"
        widgets = {
            'titre': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Votre âge', 'label': 'age'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre prenom'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre numéro de téléphone pour la reception du ticket'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'}),
            'condition': forms.CheckboxInput(attrs={'class': 'fill-control-input', 'type': 'checkbox'})
        }
