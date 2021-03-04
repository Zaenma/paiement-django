from django.db import models
from django.contrib import admin
# Create your models here.

from voyages.models import Ville, Ile


class Agence(models.Model):
    TYPE_AGENCE = (
        ('AV', 'Avion'),
        ('BA', 'Bateau'),
        ('BU', 'Bus'),
    )
    nom = models.CharField(max_length=50, verbose_name='Nom')
    telephoneFixe = models.CharField(
        max_length=50, verbose_name='Téléphone Fixe', null=True, blank=True)
    telephonePortable = models.CharField(
        max_length=50, verbose_name='Téléphone portable')
    adresseEmail = models.CharField(
        max_length=255, verbose_name='Adresse email', null=True, blank=True)
    villeLocalisation = models.ForeignKey(Ville, on_delete=models.CASCADE,
                                          max_length=50, verbose_name='Ville de localisation')
    ileLocalisation = models.ForeignKey(Ile, on_delete=models.CASCADE,
                                        max_length=50, verbose_name='Île de localisation')
    codepostal = models.CharField(
        max_length=50, verbose_name='Code postal', null=True, blank=True)

    typeAgence = models.CharField(choices=TYPE_AGENCE,
                                  max_length=50, verbose_name='Type de l\'agence')

    description = models.TextField(verbose_name="Description de l'agence")

    responsable = models.CharField(max_length=50, verbose_name="Responsable de l'agence", unique=True)

    dateAjout = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'integration")
    
    mdp =  models.CharField(max_length=20, blank=True, null=True, verbose_name="Mot de passe")

    dateModifiee = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification")

    def __str__(self):
        return self.nom


class AdminAgence(admin.ModelAdmin):
    pass
    list_display = ('nom', 'telephoneFixe', 'villeLocalisation',
                    'typeAgence', 'responsable',)
    list_filter = ('dateAjout',)
    search_fields = ['nom', 'typeAgence']


class MessageAgence(models.Model):
    nom = models.CharField(max_length=50, verbose_name='Nom')
    prenom = models.CharField(max_length=50, verbose_name='Prénom')
    email = models.EmailField(
        max_length=255, verbose_name="Adresse email de l'expediteur")
    destinateur = models.EmailField(
        max_length=255, verbose_name="Adresse email du destinateur")
    telephone = models.CharField(
        max_length=100, verbose_name="Téléphone de l'expediteur")
    sujet = models.CharField(max_length=255, verbose_name="Titre du message")
    message = models.TextField(verbose_name="Messages")
    dateEnvoie = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'envoie")

    def __str__(self):
        return self.expediteur


class AdminMessage(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'destinateur',
                    'sujet', 'dateEnvoie',)
    list_filter = ('dateEnvoie',)
    search_fields = ['nom', 'destinateur']


class Reponse(models.Model):
    destinateur = models.EmailField(
        max_length=255, verbose_name="Adresse email du destinateur")

    sujet = models.ForeignKey(
        MessageAgence, on_delete=models.CASCADE, max_length=255, verbose_name="Titre du message")

    reponse = models.TextField(verbose_name="Messages")

    dateEnvoie = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'envoie")


class AdminReponse(admin.ModelAdmin):
    list_display = ('destinateur', 'sujet', 'dateEnvoie',)
    list_filter = ('dateEnvoie',)
    search_fields = ['destinateur']
