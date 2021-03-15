from django import forms
from .models import MessageAgence, Agence, MessagesEnvoye


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageAgence
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email', 'type': 'email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone', 'type': 'tel'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenu du message'}),
        }



class MessageEnvoyeForm(forms.ModelForm):
    class Meta:
        model = MessagesEnvoye
        fields = "__all__"
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'email'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'cols': '', 'rows':'4'}),
        }


# formulaire de connexion

class ConnexionForm(forms.ModelForm):
    class Meta:
        model = Agence
        fields = "adresseEmail", "mdp"
        widgets = {
            'adresseEmail': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Adresse email de l\'agence', 'type': 'email', 'required': ''}),
            'mdp': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Mot de passe', 'type': 'password', 'required': ''})
        }

