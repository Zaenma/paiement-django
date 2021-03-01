from django.db import models

# Create your models here.


class Achat(models.Model):
    villeDepart = models.CharField(
        max_length=20, help_text='Ville de depart', verbose_name="Ville de depart")

    villeArrivee = models.CharField(
        max_length=20, help_text='Ville de destination', verbose_name="Ville de destination")

    dateVoyage = models.DateTimeField(verbose_name="Date de voyage")

    adresseUser = models.EmailField(
        max_length=255, verbose_name="Adresse de client")

    telephoneUser = models.CharField(
        max_length=20, verbose_name="Téléphone du client")

    prixVoyage = models.IntegerField(verbose_name="Prix du voyage")

    dateAchat = models.DateTimeField(auto_now_add=True,
                                     max_length=20, help_text="Date d'achat", verbose_name="Date d'achat")

    def __str__(self):
        return self.adresseUser
