from django.shortcuts import render
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect
# Create your views here.
from utilisateur.models import Utilisateur, AbonnesAnnuel, AbonnesMensuel, AbonnesHebdomadaire
from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu, Ile, Ville

#import qrcode
from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions

def index(request, pkv=None, pku=None, tag=None, date=None):

    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

    if Utilisateur.objects.filter(email=pku).exists():
        utilisateur = Utilisateur.objects.get(Q(email__exact=pku))
    elif AbonnesMensuel.objects.filter(codeAbonnement=pku).exists():
        utilisateur = AbonnesMensuel.objects.get(Q(codeAbonnement__exact=pku))
    elif AbonnesHebdomadaire.objects.filter(codeAbonnement=pku).exists():
        utilisateur = AbonnesHebdomadaire.objects.filter(codeAbonnement=pku).exists()
    else:
        pass

    # utilisateur = Utilisateur.objects.get(Q(email__exact=pku))

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

    datedepart = str(voyage.dateDepert)
    prix = str(voyage.prix)
    heur = str(heur)

    villedepart = Ile.objects.get(nom=voyage.villeDepart)

    villedestination = Ile.objects.get(nom=voyage.villeArrivee)

    villedepart = villedepart.nom

    villedestination = villedestination.nom

    contact_detail = ContactDetail(

        first_name=" C-Transport - Nom et Prénom : "+ utilisateur.nom + ' ' + 
        utilisateur.prenom + '; ' + 
        'Adresse E-mail : '+ utilisateur.email + '; '+
        'Téléphone : '+ utilisateur.telephone + '; '+
        'Code que du trajet : '+ voyage.codeVoyage + '; '+
        'Départ le : '+ datedepart + 
        ' à '+ villedepart +'; '+ 
        'Destination : '+ villedestination + '; '+ 
        'Trajet assuré par : '+ voyage.agencePrincipal + '; '
        'Prix du trajet : ' + prix + ' KMF' + '; ' +
        'Durée du trajet : ' + heur,  


        # last_name=utilisateur.prenom,

        # first_name_reading=prix + ' KMF',

        # datedepart=datedepart,

        # url=villedepart,
        # ville_destination=villedestination,
        # nickname=villedestination,
        # last_name_reading=villedepart,

        # tel=utilisateur.telephone,
        # email=utilisateur.email,
        # birthday=datedepart,
        # address=voyage.codeVoyage,
        # memo=heur,
        # org=voyage.agencePrincipal,
    )

    context = dict(
        contact_detail=contact_detail,
        # wifi_config=wifi_config,
        # video_id='J9go2nj6b3M',
        # google_maps_coordinates=google_maps_coordinates,
        # geolocation_coordinates=geolocation_coordinates,
        options_example=QRCodeOptions(
            size='t', border=6, error_correction='L'),
    )

    return render(request, 'ticket.html', context=context)
