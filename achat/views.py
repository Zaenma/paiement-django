from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
# Create your views here.
from utilisateur.models import Utilisateur, AbonnesAnnuel, AbonnesMensuel, AbonnesHebdomadaire
from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu, Ile, Ville

from django.http import Http404
#import qrcode
from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions

from django.core import mail
from django.core.mail import EmailMultiAlternatives
from .models import Achat

from sms import send_sms

from django.core.mail import EmailMessage

def enregistrementAchat(agence, voyage, typevoyage, userEmail, telephone):
    Achat.objects.create(agence=agence, codeVoyage=voyage, voyagetype=typevoyage, adresseUser=userEmail, telephoneUser=telephone)

def index(request, pkv=None, pku=None, tag=None):

    # date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    utilisateur=None

    if Utilisateur.objects.filter(email=pku).exists():
        utilisateur = Utilisateur.objects.get(Q(email__exact=pku))
    elif AbonnesMensuel.objects.filter(codeAbonnement=pku).exists():
        utilisateur = AbonnesMensuel.objects.get(Q(codeAbonnement__exact=pku))
    elif AbonnesHebdomadaire.objects.filter(codeAbonnement=pku).exists():
        utilisateur = AbonnesHebdomadaire.objects.filter(codeAbonnement=pku)
    elif AbonnesAnnuel.objects.filter(codeAbonnement=pku).exists():
        utilisateur = AbonnesAnnuel.objects.filter(codeAbonnement=pku)
    else:
        return render(request, 'erreur.html')

    if tag == 'AV':
        voyage = VoyagesParAvion.objects.get(pk=pkv)
        heur = voyage.dateArrivee - voyage.dateDepert
        prix = utilisateur.nombreSiegeReserve * voyage.prix
        VoyagesParAvion.objects.filter(pk=pkv).update(nombreSiege=voyage.nombreSiege-1)
        typevoyage = 'Aérien'
    elif tag == 'BA':
        voyage = VoyagesParBateau.objects.get(pk=pkv)
        heur = voyage.dateArrivee - voyage.dateDepert
        prix = utilisateur.nombreSiegeReserve * voyage.prix
        VoyagesParBateau.objects.filter(pk=pkv).update(nombreSiege=voyage.nombreSiege-1)
        typevoyage = "Maritime"
    elif tag == 'BU':
        voyage = VoyagesParBu.objects.get(pk=pkv)
        heur = voyage.dateArrivee - voyage.dateDepert
        prix = utilisateur.nombreSiegeReserve * voyage.prix
        VoyagesParBu.objects.filter(pk=pkv).update(nombreSiege=voyage.nombreSiege-1)
        typevoyage = "Terrestre"
    else:
        return render(request, 'erreur.html')

    datedepart = str(voyage.dateDepert)
    prix = str(voyage.prix)
    heur = str(heur)

    villedepart = Ile.objects.get(nom=voyage.villeDepart)

    villedestination = Ile.objects.get(nom=voyage.villeArrivee)

    villedepart = villedepart.nom

    villedestination = villedestination.nom

    enregistrementAchat(voyage.agencePrincipal, voyage.codeVoyage, typevoyage, utilisateur.email, utilisateur.telephone)

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

    )

    # Envoie du ticket par email =================================================
    sujet = "Ticket de transport de "+ villedepart + "vers " + villedestination

    from_email = "c-transport@c-transport.com"

    text_content = "Merci d'avoir choisi notre service </br>"

    destinataire = utilisateur.email

    # On envoie le QR code sous format HTML
    contenu_html = '<p><strong>C-Transport vous remercie de votre votre fidélité et vous souhaite un excellent voyage</strong> </br> {% qr_for_contact contact_detail=contact_detail size=\'S\' %} </p>'
    # On l'envoie également sous forme d'une image avec l'extension vcf
    image = "{% qr_for_contact contact_detail=contact_detail size='S' %}"
    
    message = EmailMultiAlternatives(sujet, text_content, from_email, [destinataire])
    # on enccompagne le message avec le contenu html
    message.attach_alternative(contenu_html, "text/html")
    message.attach('design.vcf', image, 'image/vcard')
    # On envoie le message avec la methode send()
    # message.send()

    send_sms(
        'un message de teste',
        '+221781607688',
        ['+221781158169'],
        fail_silently=False
    )


    context = dict(
        contact_detail=contact_detail,
        options_example=QRCodeOptions(
            size='t', border=6, error_correction='L'),
    )

    return render(request, 'ticket.html', context=context)

