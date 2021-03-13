from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'tel'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '', 'cols': '', 'rows':'4'}),
        }
