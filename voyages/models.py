from django.db import models
from django.contrib import admin


# Modèl des îles
class Ile(models.Model):
    nom = models.CharField(max_length=50)

    class Meta:
        verbose_name="Les île"

    def __str__(self):
        return self.nom

# Formatage du modèl des îles sur l'espace d'administration


class IlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ['nom']

# Modèle des villes


class Ville(models.Model):
    nom = models.CharField(max_length=50, verbose_name='Nom de la ville')
    ile = models.ForeignKey(Ile, on_delete=models.CASCADE,
                            verbose_name='île d\'où elle se situe')

    class Meta:
        verbose_name="Les ville"

    def __str__(self):
        return self.nom

# Formatages des villes sur l'espace d'administration


class VilleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ile')
    list_filter = ('ile',)
    search_fields = ['nom', 'ile']

# Modèle des voyages par avion


class VoyagesParAvion(models.Model):

    agencePrincipal = models.CharField(
        max_length=50, verbose_name='Agence')

    codeVoyage = models.CharField(
        max_length=50, verbose_name='Code de voyage (Identifiant du Voyage)')

    villeDepart = models.ForeignKey(
        Ile, verbose_name="Ville de depart", on_delete=models.CASCADE)

    villeArrivee = models.ForeignKey(
        Ile, related_name='Ville_destition', on_delete=models.RESTRICT, verbose_name='Ville de destination')

    villeEscale = models.ForeignKey(
        Ile, related_name='VilleEscae', verbose_name='Villes d\'sscale (si l\'on prevoit)', blank=True, on_delete=models.RESTRICT, null=True)

    dateDepert = models.DateTimeField(verbose_name='Date de depart')

    dateArrivee = models.DateTimeField(
        verbose_name='Date d\'arrivée à prevoir')

    dateRetour = models.DateTimeField(
        verbose_name='Date de retour', null=True, blank=True)

    nombreSiege = models.IntegerField(
        verbose_name='Total de siège disponible')

    prix = models.IntegerField(verbose_name='Prix par siège')

    bagage = models.IntegerField(
        verbose_name='Quantité de bagage autorisé', blank=True, null=True)

    dateAjoutee = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'integration ")

    dateModifiee = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification ")

    def __str__(self):
        return self.codeVoyage

    class Meta:
        verbose_name="Les voyages aérien"
# Format de l'affichage des voyages de par avion


class AdminVoyagesParAvion(admin.ModelAdmin):
    list_display = ('agencePrincipal', 'villeDepart',
                    'villeArrivee', 'dateDepert',)
    list_filter = ('villeDepart', 'agencePrincipal',)
    search_fields = ['agencePrincipal']

# Modèle des voyages par bateau


class VoyagesParBateau(models.Model):

    agencePrincipal = models.CharField(
        max_length=50, verbose_name='Agence')

    codeVoyage = models.CharField(
        max_length=50, verbose_name='Code de voyage (Identifiant du Voyage)')

    villeDepart = models.ForeignKey(
        Ile, verbose_name="Ville de depart", on_delete=models.CASCADE)

    villeArrivee = models.ForeignKey(
        Ile, related_name='Vle_destination', on_delete=models.RESTRICT, verbose_name='Ville de destination')

    villeEscale = models.ForeignKey(
        Ile, related_name='lleEscale', verbose_name='Villes d\'sscale (si l\'on prevoit)', blank=True, on_delete=models.RESTRICT, null=True)

    dateDepert = models.DateTimeField(verbose_name='Date de depart')

    dateArrivee = models.DateTimeField(
        verbose_name='Date d\'arrivée à prevoir')

    dateRetour = models.DateTimeField(
        verbose_name='Date de retour', blank=True, null=True)

    nombreSiege = models.IntegerField(
        verbose_name='Total de siège disponible')

    prix = models.IntegerField(verbose_name='Prix par siège')

    bagage = models.IntegerField(
        verbose_name='Quantité de bagage autorisé', blank=True, null=True)

    dateAjoutee = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'integration ")

    dateModifiee = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification ")

    class Meta:
        verbose_name="Les voyages maritime"
    def __str__(self):
        return self.codeVoyage

# Format d'affichage des voyages maritime


class AdminVoyageParBateau(admin.ModelAdmin):
    list_display = ('agencePrincipal', 'villeDepart',
                    'villeArrivee', 'dateDepert',)
    list_filter = ('villeDepart', 'agencePrincipal',)
    search_fields = ['agencePrincipal']

# Modèle des voyages terrestre


class VoyagesParBu(models.Model):

    agencePrincipal = models.CharField(
        max_length=50, verbose_name='Agence')

    codeVoyage = models.CharField(
        max_length=50, verbose_name='Code de voyage (Identifiant du Voyage)')

    villeDepart = models.ForeignKey(
        Ville, verbose_name="Ville de départ", on_delete=models.CASCADE)

    ile = models.ForeignKey(
        Ile, verbose_name="Ile : un voyage terrestre", on_delete=models.CASCADE)

    villeArrivee = models.ForeignKey(
        Ville, related_name='Ville_desnation', on_delete=models.RESTRICT, verbose_name='Ville de destination')

    villeEscale = models.ForeignKey(
        Ville, related_name='VilleEcale', verbose_name='Villes d\'sscale (si l\'on prevoit)', blank=True, on_delete=models.RESTRICT, null=True)

    dateDepert = models.DateTimeField(verbose_name='Date de départ')

    dateArrivee = models.DateTimeField(
        verbose_name='Date d\'arrivée à prevoir', blank=True, null=True)

    nombreSiege = models.IntegerField(
        verbose_name='Total de sièges disponible')

    prix = models.IntegerField(verbose_name='Prix par siège')

    bagage = models.IntegerField(
        verbose_name='Quantité de bagages autorisées', blank=True, null=True)

    dateAjoutee = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'integration ")

    dateModifiee = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification ")

    class Meta:
        verbose_name="Les voyages terrestres"
    def __str__(self):
        return self.codeVoyage

# Format d'affichages des voyages terrestre


class AdminVoyageParBus(admin.ModelAdmin):
    list_display = ('agencePrincipal', 'villeDepart',
                    'villeArrivee', 'dateDepert',)
    list_filter = ('villeDepart', 'agencePrincipal',)
    search_fields = ['agencePrincipal']

# ============================================================================

# Modèle de pour le formulaire de recherche de biellet d'avion


class ModelAvion(models.Model):
    typev = models.CharField(max_length=50)
    ville_depart = models.ForeignKey(
        Ile, max_length=50, on_delete=models.CASCADE, related_name='Vile_desnation')
    ville_destination = models.ForeignKey(
        Ile, max_length=50, on_delete=models.CASCADE, related_name='Vile_dstination')
    date_depart = models.DateTimeField()
    date_retour = models.DateTimeField(blank=True, null=True)


# Modèle pour le formulaire de recherche de billets de bateau
class ModelBateau(models.Model):
    typev = models.CharField(max_length=50)
    ville_depart = models.ForeignKey(
        Ile, max_length=50, on_delete=models.CASCADE, related_name='Vile_destinaion')
    ville_destination = models.ForeignKey(
        Ile, max_length=50, on_delete=models.CASCADE, related_name='Vile_destinatin')
    date_depart = models.DateTimeField()
    date_retour = models.DateTimeField(blank=True, null=True)

# Modèle pour le formulaire de recherche de ticket de bus


class ModelBus(models.Model):
    typev = models.CharField(max_length=50)
    ile = models.ForeignKey(Ile, on_delete=models.CASCADE, max_length=50)
    ville_depart = models.ForeignKey(
        Ville, on_delete=models.CASCADE, max_length=50)
    ville_destination = models.ForeignKey(Ville, related_name='Vile_destination',
                                          on_delete=models.CASCADE)

    date_depart = models.DateTimeField()
    date_retour = models.DateTimeField(blank=True, null=True)
