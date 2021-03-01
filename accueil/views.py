from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu
from agence.models import Agence
from voyages.formulaire import AvionForm, BateauForm, BusForm
from django.shortcuts import render, redirect
import datetime
# Les imports de l'application


def index(request):
    # les formulaire de recherches
    avion = AvionForm()
    bateau = BateauForm()
    bus = BusForm()
    
    heurbateau = VoyagesParBateau.objects.filter(
        dateArrivee__gte=datetime.date.today())
    heuravion = VoyagesParAvion.objects.filter(
        dateArrivee__gte=datetime.date.today())
    heurbus = VoyagesParBu.objects.filter(
        dateArrivee__gte=datetime.date.today())
        
    agence = Agence.objects.all()

    # le dictionnaire à envoyer dans le template
    donnees = {'av': avion, 'ba': bateau, 'bu': bus,
               'agence': agence, 'heurbateau': heurbateau, 'heuravion': heuravion, 'heurbus': heurbus}
    return render(request, 'index.html', donnees)
