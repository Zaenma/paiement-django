from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from .formulaire import AvionForm, BateauForm, BusForm, RechercheForm
from agence.models import Agence
from voyage_prevu.models import VoyagesPrevu, Ile, Ville


def index(request):
    # les formulaire de recherches
    avion = AvionForm()
    bateau = BateauForm()
    bus = BusForm()

    # recupération des agences pour les afficher dans le ménu
    agences = Agence.objects.all()

    # le dictionnaire à envoyer dans le template
    donnees = {'av': avion, 'ba': bateau, 'bu': bus, 'ags': agences}

    # le template
    return render(request, 'index.html', donnees)


def recherche(request):
    # recupération des agences pour les afficher dans le ménu
    agences = Agence.objects.all()

    date_depart = request.GET["date_depart"]
    message = None
    nombre_voyage = 0
    ville_depart = Ville.objects.get(pk=request.GET["ville_depart"])

    ville_destination = Ville.objects.get(
        pk=request.GET["ville_destination"])

    # condition pour les bus
    if request.GET["typev"] == 'BU':
        ile = Ile.objects.get(pk=request.GET["ile"])
        voyagesPrevu = VoyagesPrevu.objects.filter(
            Q(villeDepart__exact=ville_depart) &
            Q(villeArrivee__exact=ville_destination) &
            Q(dateDepert__contains=date_depart) &
            Q(typeVoyage__contains="BU") &
            Q(ile__exact=ile))
        nombre_voyage = voyagesPrevu.count()
        message = "1"

    # si le moyen de transport demander est maritime
    if request.GET["typev"] == 'BA':
        voyagesPrevu = VoyagesPrevu.objects.filter(
            Q(villeDepart__exact=ville_depart) &
            Q(villeArrivee__exact=ville_destination) &
            Q(dateDepert__contains=request.GET["date_depart"]),
            Q(typeVoyage__exact='BA'))

        nombre_voyage = voyagesPrevu.count()
        message = "1"

    # sinon si le moyen de transport demander est aérien
    if request.GET["typev"] == 'AV':
        voyagesPrevu = VoyagesPrevu.objects.filter(
            Q(villeDepart__exact=ville_depart) &
            Q(villeArrivee__exact=ville_destination) &
            Q(dateDepert__contains=request.GET["date_depart"]),
            Q(typeVoyage__exact='AV'))

        nombre_voyage = voyagesPrevu.count()
        message = "1"

    # sinon si le moyen de transport demander est aérien
    if request.GET["typev"] == 'RE':
        voyagesPrevu = VoyagesPrevu.objects.filter(
            Q(villeDepart__exact=ville_depart) &
            Q(villeArrivee__exact=ville_destination) &
            Q(dateDepert__contains=request.GET["date_depart"]))

        nombre_voyage = voyagesPrevu.count()
        message = "1"

    # dictionnaire des données
    donnees = {'vps': voyagesPrevu,
               'msg': message,
               'nbv': nombre_voyage, 'ags': agences}

    if nombre_voyage == 0:
        voyagesPrevu = VoyagesPrevu.objects.all()
        nombre_voyage = voyagesPrevu.count()
        message = 0
        recherche = RechercheForm()
        donnees = {'vps': voyagesPrevu,
                   'msg': message,
                   'nbv': nombre_voyage, 're': recherche, 'ags': agences}

    pagination = Paginator(voyagesPrevu, 5)
    nombre_page = request.GET.get('page')
    voyagesPrevu = pagination.get_page(nombre_page)

    return render(request, 'resultat-recherche.html', donnees)
