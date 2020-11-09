from django import forms
from .models import Utilisateur


class UserForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ('nom', 'prenom', 'telephone', 'email')
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
