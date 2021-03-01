from django.db import models
from django.contrib import admin
from django import forms
# Create your models here.


class Utilisateur(models.Model):

    nom = models.CharField(
        max_length=20, help_text='Nom du client', verbose_name='Nom')

    prenom = models.CharField(
        max_length=20, help_text='Prenom du client', verbose_name='Prénom')

    dateNaissance = models.DateField(
        max_length=20, help_text='Date de nissance', verbose_name='Date de naissance')

    email = models.CharField(
        max_length=100, help_text='Adresse e-mail', verbose_name='E-mail')

    telephone = models.CharField(
        max_length=20, help_text='Téléphone principale', verbose_name='Téléphone')

    telephoneSupplementaire = models.CharField(
        max_length=20, help_text='Téléphone secondaire', verbose_name='Autre Téléphone supplémentaire', null=True, blank=True)

    condition = models.BooleanField(
        help_text='Conditions d\'utilisation', verbose_name='Condition d\'utilisation')

    # Information du voyages
    nombreSiegeReserve = models.IntegerField(
        help_text='Nombre de sièges', verbose_name='Nombre de place à réserver', default=1)

    recevoirAlert = models.BooleanField(
        help_text="Envoie d'alerte", verbose_name='Reception des alertes', default=False)

    dateEngregistrement = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'inscription")

    class Meta:
        verbose_name="Les Clients"

    def __str__(self):
        return self.nom


class AdminUtilisateur(admin.ModelAdmin):
    list_display = ('nom', 'prenom',
                    'telephone', 'email', 'dateEngregistrement',)
    list_filter = ('dateEngregistrement',)
    search_fields = ['nom', 'prenom']


# classe personne qui ne sera pas instancié

class Personne(models.Model):
    nom = models.CharField(
        max_length=20, help_text='Nom du client', verbose_name='Nom')

    prenom = models.CharField(
        max_length=20, help_text='Prenom du client', verbose_name='Prénom')

    codeAbonnement = models.CharField(
        max_length=20, help_text="Code d'abonnement", verbose_name="Code d'abonnement", unique=True)

    dateNaissance = models.DateField(
        max_length=20, help_text='Date de nissance', verbose_name='Date de naissance')

    email = models.CharField(
        max_length=100, help_text='Adresse e-mail', verbose_name='E-mail')

    telephone = models.CharField(
        max_length=20, help_text='Téléphone principale', verbose_name='Téléphone')

    nombreVoyageParMois = models.IntegerField(
        help_text='Nombre de voyags', verbose_name='Nombre de voyages par mois', blank=True, null=True)

    dateAbonnement = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'abonnement")

    montantMensuelVerse = models.IntegerField(
        help_text='Montant par mois', verbose_name='Montant minimum à verser par mois')


    class Meta:
        abstract = True


class AbonnesMensuel(Personne):

    def __str__(self):
       return self.nom

    class Meta:
        verbose_name="Abonnements mensuel"
    pass

class AdminAbonnesMensuel(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'codeAbonnement', 'dateAbonnement',)
    list_filter = ('dateAbonnement',)
    search_fields = ['nom']
    pass

class AbonnesAnnuel(Personne):
    class Meta:
        verbose_name="Adonnements mensuel"
        
    def __str__(self):
       return self.nom
    pass

class AdminAbonnesAnnuel(admin.ModelAdmin):
    # list_display = ('nom', 'prenom', 'telephone', 'dateAbonnement',)
    # list_filter = ('dateAbonnement',)
    # search_fields = ['nom']
    pass

class Versemmenrts(models.Model):
    montantMensuelVerse = models.IntegerField(
        help_text='Montant versé', verbose_name='Montant versé')
    dateVersement = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de versement")

    class Meta:
        abstract = True

class VersementsAbonneAnnuel(Versemmenrts):
    abonneAnuuel = models.ForeignKey(AbonnesAnnuel, on_delete=models.CASCADE, help_text='Abonné annuel', verbose_name='Abonné annuel')
    
    class Meta:
        verbose_name="Versement des adonnements annuel"

    def __str__(self):
       return str(self.abonneAnuuel)

class AdminVersementsAbonneAnnuel(admin.ModelAdmin):
    list_display = ('abonneAnuuel', 'montantMensuelVerse', 'dateVersement',)
    list_filter = ('dateVersement',)
    search_fields = ['abonneAnuuel']

class VersementsAbonneMensuel(Versemmenrts):
    abonneMensuel = models.ForeignKey(AbonnesMensuel, on_delete=models.CASCADE, help_text='Abonné menuel', verbose_name='Abonné maensuel')
    def __str__(self):
       return str(self.abonneMensuel)

    class Meta:
        verbose_name="Versement des adonnements mensuel"
    pass

class AdminVersementsAbonneMensuel(admin.ModelAdmin):
    list_display = ('abonneMensuel', 'montantMensuelVerse', 'dateVersement',)
    list_filter = ('dateVersement',)
    search_fields = ['abonneMensuel']


# modèle du formulare de recherche
class AbonneModel(models.Model):
    codeAbonnement = models.CharField(
        max_length=20, help_text="Code d'abonnement", verbose_name="Code d'abonnement", unique=True)
    nombrePlace = models.IntegerField(default=1)


