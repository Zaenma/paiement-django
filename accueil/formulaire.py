from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrer l\'dresse email', 'type': 'email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone', 'type': 'tel'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenu du message', 'cols': '', 'rows':'4'}),
        }
