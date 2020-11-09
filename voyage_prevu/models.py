from django.db import models
from django.contrib import admin
from agence.models import Agence


class Ile(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class IlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    list_filter = ('nom',)
    search_fields = ['nom']


class Ville(models.Model):
    nom = models.CharField(max_length=50)
    ile = models.ForeignKey(Ile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nom)


class VilleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'ile')
    list_filter = ('nom', 'ile',)
    search_fields = ['nom', 'ile']


# Modèle des voyages

class VoyagesPrevu(models.Model):

    TYPE_VOYAGE = [
        ('BA', 'Bateau'),
        ('AV', 'Avion'),
        ('BU', 'Bus'),
    ]

    agencePrincipal = models.ForeignKey(
        Agence, verbose_name='Agence Organisatrice du voyage', on_delete=models.CASCADE)

    codeVoyage = models.CharField(
        max_length=50, verbose_name='Code de voyage (Identifiant du Voyage)')

    villeDepart = models.ForeignKey(
        Ville, verbose_name="Ville de départ", on_delete=models.CASCADE)

    ile = models.ForeignKey(
        Ile, verbose_name="Ile : si c'est une voyage terrestre", on_delete=models.CASCADE, blank=True)

    villeArrivee = models.ForeignKey(
        Ville, related_name='Ville_destination', on_delete=models.RESTRICT, verbose_name='Ville de destination')

    villeEscale = models.ForeignKey(
        Ville, related_name='VilleEscale', verbose_name='Villes d\'sscale (si l\'on prevoit)', blank=True, on_delete=models.RESTRICT)

    typeVoyage = models.CharField(
        max_length=20, choices=TYPE_VOYAGE, verbose_name='Moyen de transport')

    dateDepert = models.DateTimeField(verbose_name='Date de départ')

    datearrivee = models.DateTimeField(
        verbose_name='Date d\'arrivée à prevoir', blank=True, null=True)

    dateretour = models.DateTimeField(
        verbose_name='Date d\'arrivée à prevoir', blank=True)

    nombreSiege = models.IntegerField(
        verbose_name='Total de siège disponible', blank=True)

    prix = models.IntegerField(verbose_name='Prix par siège')

    bagage = models.IntegerField(
        verbose_name='Quantité de bagage autorisé', blank=True)

    def __str__(self):
        return self.codeVoyage


class VoyagesPrevuAdmin(admin.ModelAdmin):
    # list_display = ('agencePrincipal',)
    list_filter = ('agencePrincipal',)
    search_fields = ['agencePrincipal']
