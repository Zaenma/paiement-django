from django.db import models
from django.contrib import admin


class TypeAgence(models.Model):
    TYPE_VOYAGE = [
        ('Bateau', 'Agence de voyage maritime'),
        ('Avion', 'Agence de voyage aérien'),
        ('bus', 'Agence de voyage terrestre'),
    ]
    nom = models.CharField(
        max_length=50, choices=TYPE_VOYAGE, verbose_name='Type d\'agence')

    def __str__(self):
        return self.nom


class Agence(models.Model):
    nom = models.CharField(max_length=50, verbose_name='Nom de l\'agence')

    typeAgence = models.ForeignKey(
        TypeAgence, verbose_name="Type d'agence", on_delete=models.CASCADE)

    telephone = models.CharField(
        max_length=50, verbose_name='Téléphone de l\'agence')

    email = models.EmailField(
        max_length=254, verbose_name='Adresse email de \'agence')

    codePostal = models.CharField(
        max_length=10, verbose_name='Code postal', null=True)

    created_at = models.DateTimeField(
        auto_now=False, auto_now_add=True, verbose_name='Date d\'enregistrement')

    def __str__(self):
        return self.nom


class AgenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'typeAgence', 'telephone')
    list_filter = ('nom', 'typeAgence', 'telephone',)
    search_fields = ['nom', 'typeAgence']
