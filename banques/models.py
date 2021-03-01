from django.db import models

from django.contrib import admin
# Create your models here.
from agence.models import Agence

class Donnees(models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.RESTRICT, verbose_name='Agence')

    dateVente = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'achat")

    montantDeVente = models.IntegerField(verbose_name="Montant de l'achat")

    class Meta:
        abstract = True



class Banque(Donnees):

    reduction = models.IntegerField(default=20, verbose_name="Taux de réduction")
    
    class Meta:
        verbose_name = "Banque principale"

    def __str__(self):
        return str(self.agence)

class AdminBanque(admin.ModelAdmin):
    list_display = ('agence', 'dateVente', 'montantDeVente','reduction',)
    list_filter = ('dateVente',)
    search_fields = ['agence']
    


# statistique des agences 
class StatistiqueVente(Donnees):
    pass

    def __str__(self):
        return str(self.agence)

    class Meta:
        verbose_name = "Statistiques des vente"
    
class AdminStatistique(admin.ModelAdmin):
    list_display = ('agence', 'dateVente', 'montantDeVente',)
    list_filter = ('dateVente',)
    search_fields = ['agence']