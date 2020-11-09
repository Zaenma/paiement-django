from django.db import models
from voyage_prevu.models import Ville, Ile
from agence.models import Agence


class ModelAvion(models.Model):
    typev = models.CharField(max_length=50)
    ville_depart = models.ForeignKey(
        Ville, max_length=50, on_delete=models.CASCADE, related_name='Vile_desnation')
    ville_destination = models.ForeignKey(
        Ville, max_length=50, on_delete=models.CASCADE, related_name='Vile_dstination')
    date_depart = models.DateTimeField()


class ModelBateau(models.Model):
    typev = models.CharField(max_length=50)
    ville_depart = models.ForeignKey(
        Ville, max_length=50, on_delete=models.CASCADE, related_name='Vile_destinaion')
    ville_destination = models.ForeignKey(
        Ville, max_length=50, on_delete=models.CASCADE, related_name='Vile_destinatin')
    date_depart = models.DateTimeField()


class ModelBus(models.Model):
    typev = models.CharField(max_length=50)
    ile = models.ForeignKey(Ile, on_delete=models.CASCADE, max_length=50)
    ville_depart = models.ForeignKey(
        Ville, on_delete=models.CASCADE, max_length=50)
    ville_destination = models.ForeignKey(Ville, related_name='Vile_destination',
                                          on_delete=models.CASCADE)

    date_depart = models.DateTimeField()


class Recherche(models.Model):
    typev = models.CharField(max_length=50)
    ville_depart = models.ForeignKey(
        Ville, max_length=50, on_delete=models.CASCADE, related_name='Vile_deation')
    ville_destination = models.ForeignKey(
        Ville, max_length=50, on_delete=models.CASCADE, related_name='Vile_dsation')
    date_depart = models.DateTimeField()
