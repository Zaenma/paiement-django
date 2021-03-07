from django.db import models
from django.contrib import admin
# Create your models here.


class Contact(models.Model):

    nom = models.CharField(max_length=50, verbose_name='Nom complet')

    telephone = models.CharField(max_length=50, verbose_name='Téléphone portable')
    

    email = models.EmailField(max_length=255, verbose_name='Adresse email', null=True, blank=True)

    sujet = models.TextField(verbose_name="Titre du message")

    message = models.TextField(verbose_name="Message complet")

    dateAjout = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'integration")


    class Meta:
        verbose_name="Message"

    def __str__(self):
        return self.nom


class AdminContact(admin.ModelAdmin):
    pass
    list_display = ('nom', 'telephone', 'sujet','dateAjout',)
    list_filter = ('dateAjout',)
    search_fields = ['nom']

