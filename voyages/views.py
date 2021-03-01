from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
from .models import VoyagesParBu, VoyagesParBateau, VoyagesParAvion, Ville, Ile


def voyages(request):
    """
    SI la variable typev en GET est AV, on cherche les voyages dans la table des voyages par Avion
    et on vérifie que les champs corresponds bien aux entrés de l'utilisateur
    """
    nombre_voyage = 0
    if request.GET["typev"] == 'AV':
        voyages = VoyagesParAvion.objects.filter(
            Q(villeDepart__exact=request.GET["ville_depart"]) &
            Q(villeArrivee__exact=request.GET["ville_destination"]) &
            Q(dateDepert__contains=request.GET["date_depart"])
        )
        nombre_voyage = voyages.count()
        voyages = {'voyages': voyages,
                   'nombre_voyage': nombre_voyage, 'tag': request.GET["typev"]}

    if request.GET["typev"] == 'BA':
        voyages = VoyagesParBateau.objects.filter(
            Q(villeDepart__exact=request.GET["ville_depart"]) &
            Q(villeArrivee__exact=request.GET["ville_destination"]) &
            Q(dateDepert__contains=request.GET["date_depart"])
        )
        nombre_voyage = voyages.count()
        voyages = {'voyages': voyages, 'tag': request.GET["typev"]}

    if request.GET["typev"] == 'BU':
        voyages = VoyagesParBu.objects.filter(
            Q(villeDepart__exact=request.GET["ville_depart"]) &
            Q(Q(villeArrivee__exact=request.GET["ville_destination"]) | Q(villeEscale__exact=request.GET["ville_destination"])) &
            Q(ile__exact=request.GET["ile"]) &
            Q(dateDepert__contains=request.GET["date_depart"])
        )
        nombre_voyage = voyages.count()
        voyages = {'voyages': voyages,
                   'nombre_voyage': nombre_voyage, 'tag': request.GET["typev"]}

    """
    Si on a pas de voyage pour les critère que l'utilisateur a donné,
    on lui propose les voyages qui sont prévus 3 jours après la date qu'il a
    donnée en tenant compte les villes et 3 jours avant sans depasser la date du jour
    """
    if nombre_voyage == 0:
        # la date de jour exclue l'heure
        datedujour = datetime.datetime.now()
        datedujour = datedujour.date()

        # la date de l'utilisateur
        date = request.GET["date_depart"]

        # Trois jours après la date qu'il a donné
        troisjoursapres = datetime.datetime.strptime(date, "%Y-%m-%d").date() + \
            datetime.timedelta(days=3)

        # Trois jours avant la date de l'utilisateur
        troisjursavant = datetime.datetime.strptime(date, "%Y-%m-%d").date() - \
            datetime.timedelta(days=3)

        # Si les trois jours avant la date de l'utilisateur depasse la date du jour, on arrête à la date du jour, troisjoursavant = datedujour
        if troisjursavant < datedujour:
            troisjursavant = datedujour

        # Maintenant on va prendre les voyages qui dont la date de depart est supérieur à la date de troisjoursavant et ceux dont la date de depart est inférieur à la date troisjoursapres

        if request.GET["typev"] == 'AV':
            voyages = VoyagesParAvion.objects.filter(
                Q(villeDepart__exact=request.GET["ville_depart"]) &
                Q(villeArrivee__exact=request.GET["ville_destination"]) &
                Q(Q(dateDepert__lte=troisjoursapres)
                  & Q(dateDepert__gte=troisjursavant))
            )
            # Nombre de voyage trouvé
            nombre_voyage = voyages.count()
            # Distionnaire à renvoyer
            voyages = {'voyages': voyages,
                       'nombre_voyage': nombre_voyage, 'tag': request.GET["typev"]}

        if request.GET["typev"] == 'BA':
            voyages = VoyagesParBateau.objects.filter(
                Q(villeDepart__exact=request.GET["ville_depart"]) &
                Q(villeArrivee__exact=request.GET["ville_destination"]) &
                Q(Q(dateDepert__lte=troisjoursapres)
                  & Q(dateDepert__gte=troisjursavant))
            )

            # Nombre de voyage trouvé
            nombre_voyage = voyages.count()
            # Distionnaire à renvoyer
            voyages = {'voyages': voyages,
                       'nombre_voyage': nombre_voyage, 'tag': request.GET["typev"]}

        # Pour les bus en cas de manque de voyage pour les informations de l'utilisateur
        if request.GET["typev"] == 'BU':
            voyages = VoyagesParBateau.objects.filter(
                Q(villeDepart__exact=request.GET["ville_depart"]) &
                Q(villeArrivee__exact=request.GET["ville_destination"]) &
                Q(ile__exact=request.GET["ile"]) &
                Q(Q(dateDepert__lte=troisjoursapres)
                  & Q(dateDepert__gte=troisjursavant))
            )

            # Nombre de voyage trouvé
            nombre_voyage = voyages.count()
            # Distionnaire à renvoyer
            voyages = {'voyages': voyages,
                       'nombre_voyage': nombre_voyage, 'tag': request.GET["typev"]}

    return render(request, 'voyages.html', voyages)
