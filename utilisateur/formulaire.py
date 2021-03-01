from django import forms
from .models import Utilisateur, AbonneModel
from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu, Ville, Ile


class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'dateNaissance': forms.DateInput(attrs={'class': 'form-control', 'placeholder': '', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'telephoneSupplementaire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'nombreSiegeReserve': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'condition': forms.CheckboxInput(attrs={'class': 'fill-control-input', 'type': 'checkbox'}),
            'recevoirAlert': forms.CheckboxInput(attrs={'class': 'fill-control-input', 'type': 'checkbox'}),
        }


class VoyagesParAvionForm(forms.ModelForm):
    class Meta:
        model = VoyagesParAvion
        fields = "__all__"
        widgets = {
            'agencePrincipal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Le nom de l\'agence'}),
            'codeVoyage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code de voyage'}),
            'villeDepart': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ville de depart'}),
            'villeArrivee': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ville de destination'}),
            'villeEscale': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ville d\'esacale'}),
            'dateDepert': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date de depart', 'type': 'datetime-local'}),
            'dateArrivee': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date d\'arrivée', 'type': 'datetime-local'}),
            'dateRetour': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date de retour', 'type': 'datetime-local'}),
            'nombreSiege': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de sièges disponible'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix par siège'}),
            'bagage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité de bagages autorisées'}),
        }


class VoyagesParBateauForm(forms.ModelForm):
    class Meta:
        model = VoyagesParBateau
        fields = "__all__"
        widgets = {
            'agencePrincipal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Le nom de l\'agence'}),
            'codeVoyage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code de voyage'}),
            'villeDepart': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ville de depart'}),
            'villeArrivee': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ville de destination'}),
            'villeEscale': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ville d\'esacale'}),
            'dateDepert': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date de depart', 'type': 'datetime-local'}),
            'dateArrivee': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date d\'arrivée', 'type': 'datetime-local'}),
            'dateRetour': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date de retour', 'type': 'datetime-local'}),
            'nombreSiege': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de sièges disponible'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix par siège'}),
            'bagage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité de bagages autorisées'}),
        }


class VilleForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'ile': forms.Select(attrs={'class': 'form-control'}),
        }


class IleForm(forms.ModelForm):
    class Meta:
        model = Ile
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'île'}),
        }



# Formulaire de recherche d'un abonné

class AbonneForm(forms.ModelForm):
    class Meta:
        model = AbonneModel
        fields = "__all__"
        widgets = {
            'codeAbonnement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Code d'abonnement"}),
            'nombrePlace': forms.NumberInput(attrs={'class': 'form-control'}),
        }
