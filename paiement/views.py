from django.shortcuts import render
from django.db.models import Q
import datetime
# Create your views here.
from utilisateur.models import Utilisateur, AbonnesAnnuel
from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu


def paiement(request, pkv, pku, tag, date):

    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

    utilisateur = Utilisateur.objects.get(Q(email__exact=pku))
    
    # utilisateur = Utilisateur.objects.get(Q(email__exact=pku) & Q(dateEngregistrement__contains=date))

    if tag == 'AV':
        voyage = VoyagesParAvion.objects.get(pk=pkv)

        heur = voyage.dateArrivee - voyage.dateDepert

        prix = utilisateur.nombreSiegeReserve * voyage.prix

    if tag == 'BA':
        voyage = VoyagesParBateau.objects.get(pk=pkv)

        heur = voyage.dateArrivee - voyage.dateDepert

        prix = utilisateur.nombreSiegeReserve * voyage.prix

    if tag == 'BU':
        voyage = VoyagesParBu.objects.get(pk=pkv)

        heur = voyage.dateArrivee - voyage.dateDepert

        prix = utilisateur.nombreSiegeReserve * voyage.prix

    donnees = {'user': utilisateur,
               'voyage': voyage, 'heur': heur, 'prix': prix, 'pkv': pkv, 'pku': pku, 'tag': tag, 'date': date}

    return render(request, 'paiement.html', donnees)
