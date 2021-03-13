from django.db import models
from django.contrib import admin
# Create your models here.

class Achat(models.Model):

    agence = models.CharField(verbose_name="Agence", max_length=20)
    codeVoyage = models.CharField(verbose_name="Code de voyage", max_length=20)
    voyagetype = models.CharField(verbose_name="Type de voyage", max_length=20)
    adresseUser = models.EmailField(
        max_length=255, verbose_name="Adresse de client")

    telephoneUser = models.CharField(
        max_length=20, verbose_name="Téléphone du client")

    dateAchat = models.DateTimeField(auto_now_add=True,
                                     max_length=20, help_text="Date d'achat", verbose_name="Date d'achat")

    def __str__(self):
        return self.adresseUser

class AdminAchat(admin.ModelAdmin):
    list_display = ('agence', 'codeVoyage',
                    'voyagetype', 'adresseUser','dateAchat')
    list_filter = ('dateAchat',)
    search_fields = ['agence', 'codeVoyage']
