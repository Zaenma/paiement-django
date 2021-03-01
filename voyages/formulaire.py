from django import forms
from .models import ModelAvion, ModelBateau, ModelBus


class AvionForm(forms.ModelForm):
    class Meta:
        model = ModelAvion
        fields = "__all__"
        widgets = {
            'typev': forms.TextInput(attrs={'value': 'AV', 'type': 'hidden'}),
            'ville_depart': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'ville_destination': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
            'date_retour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
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
            'date_retour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
        }


class BusForm(forms.ModelForm):
    class Meta:
        model = ModelBus
        fields = "__all__"
        widgets = {
            'typev': forms.TextInput(attrs={'value': 'BU', 'type': 'hidden'}),
            'ile': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'ville_depart': forms.Select(attrs={'class': 'form-control', 'placeholder': '', 'v-model': 'message'}),
            'ville_destination': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
            'date_retour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
        }

