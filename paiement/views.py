from django.shortcuts import render
from django.db.models import Q
import datetime
from paypal.standard.forms import PayPalPaymentsForm

import stripe # new

from django.conf import settings
from django.views.generic.base import TemplateView

from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY # new

# Create your views here.
from utilisateur.models import Utilisateur, AbonnesAnnuel, AbonnesMensuel, AbonnesHebdomadaire
from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu

def paiement(request, pkv, pku, tag):

    # date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    # utilisateur = Utilisateur.objects.get(Q(email__exact=pku))
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

    # utilisateur = Utilisateur.objects.get(Q(email__exact=pku) & Q(dateEngregistrement__contains=date))

    if VoyagesParAvion.objects.filter(pk=pkv).exists():
        voyage = VoyagesParAvion.objects.get(pk=pkv)
    elif VoyagesParBateau.objects.filter(pk=pkv).exists():
        voyage = VoyagesParBateau.objects.filter(pk=pkv)
    elif VoyagesParBu.objects.filter(pk=pkv).exists():
        voyage = VoyagesParBu.objects.filter(pk=pkv)
    else:
        return render(request, 'erreur.html')

    if tag == 'AV':
        heur = voyage.dateArrivee - voyage.dateDepert
        prix = utilisateur.nombreSiegeReserve * voyage.prix
        prix = prix/493
        prix_visa = prix * 1.2 * 100
        prix_visa_info = prix * 1.2

    elif tag == 'BA':
        heur = voyage.dateArrivee - voyage.dateDepert
        prix = utilisateur.nombreSiegeReserve * voyage.prix
        prix = prix/493
        prix_visa = prix * 1.2 * 100
        prix_visa_info = prix * 1.2

    elif tag == 'BU':
        heur = voyage.dateArrivee - voyage.dateDepert
        prix = utilisateur.nombreSiegeReserve * voyage.prix
        prix = prix/493
        prix_visa = prix * 1.2 * 100
        prix_visa_info = prix * 1.2
    else:
        return render(request, 'erreur.html')


    paypal_dict = {
        "business": "zaenma.halidisalim@gmail.com",
        "amount": prix,
        "item_name": "Ticket de transport",
        "invoice": "unique-invoice-id",
        "currency_code": "EUR",
        "return": request.build_absolute_uri(reverse('achat:success', kwargs={'pkv': pkv, 'pku': pku, 'tag': tag})),
        
        "notify_url": request.build_absolute_uri(reverse('achat:success', kwargs={'pkv': pkv, 'pku': pku, 'tag': tag})),

        # "notify_url": request.build_absolute_uri(reverse('achat:success', kwargs={'pkv': request.GET['pkv'], 'pku': request.GET['pku'], 'tag': request.GET['tag']})),
        "cancel_return": request.build_absolute_uri(reverse('paiement:paiement', kwargs={'pkv': pkv, 'tag': tag, 'pku': pku})),
        # "cancel_return": request.build_absolute_uri(reverse('paiement:paiement', kwargs={'pkv': pkv, 'tag': tag, 'pku': pku, 'date': datetime.datetime.now()})),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    donnees = {'user': utilisateur,
               'voyage': voyage, 'heur': heur, 
               'prix': prix, 'pkv': pkv, 'pku': pku, 
               'tag': tag, 'formPaypal': form, 
               'prix_visa': prix_visa,
               'prix_visa_info': prix_visa_info,
               'key': settings.STRIPE_PUBLISHABLE_KEY}

    return render(request, 'paiement.html', donnees)
