from django.db import models
from django.contrib import admin

from agence.models import Agence
from voyage_prevu.models import VoyagesPrevu


class Utilisateur(models.Model):
    pass
    TITRE = [
        ('Monsieur', 'Monsieur'),
        ('Madame', 'Madame'),
    ]

    titre = models.CharField(
        choices=TITRE, max_length=30, verbose_name="Titre")

    age = models.IntegerField(verbose_name='Age')

    nom = models.CharField(max_length=30, verbose_name="Nom")

    prenom = models.CharField(max_length=30, verbose_name="Prénom")

    telephone = models.CharField(max_length=30, verbose_name="Téléphone")

    email = models.EmailField(max_length=255, verbose_name="Adresse email")

    condition = models.BooleanField(
        verbose_name="Condition d'utilisation", default=True)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Date d\'enregistrement')

    def __str__(self):
        return self.nom


class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nom', 'prenom', 'telephone', 'created_at')
    list_filter = ('titre', 'created_at', )
    search_fields = ['nom', 'prenom']


class ResponsablesAgence(models.Model):
    pass
