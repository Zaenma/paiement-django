from django import forms
from .models import ModelAvion, ModelBateau, ModelBus, Recherche


class AvionForm(forms.ModelForm):
    class Meta:
        model = ModelAvion
        fields = "__all__"
        widgets = {
            'typev': forms.TextInput(attrs={'value': 'AV', 'type': 'hidden'}),
            'ville_depart': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'ville_destination': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
        }


class BateauForm(forms.ModelForm):
    class Meta:
        model = ModelBateau
        fields = "__all__"
        widgets = {
            'typev': forms.TextInput(attrs={'value': 'BA', 'type': 'hidden'}),
            'ville_depart': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'ville_destination': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
        }


class BusForm(forms.ModelForm):
    class Meta:
        model = ModelBus
        fields = "__all__"
        widgets = {
            'typev': forms.TextInput(attrs={'value': 'BU', 'type': 'hidden'}),
            'ile': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'ville_depart': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'ville_destination': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
        }


class RechercheForm(forms.ModelForm):
    class Meta:
        model = Recherche
        fields = "__all__"
        widgets = {
            'typev': forms.TextInput(attrs={'value': 'RE', 'type': 'hidden'}),
            'ville_depart': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'ville_destination': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
        }
