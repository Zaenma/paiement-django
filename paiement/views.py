from django.shortcuts import render
from django.db.models import Q
import datetime
from paypal.standard.forms import PayPalPaymentsForm


# from django.core.urlresolvers import reverse
from django.urls import reverse

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

        prix = prix/493

    if tag == 'BA':
        voyage = VoyagesParBateau.objects.get(pk=pkv)

        heur = voyage.dateArrivee - voyage.dateDepert

        prix = utilisateur.nombreSiegeReserve * voyage.prix

        prix = prix/493

    if tag == 'BU':
        voyage = VoyagesParBu.objects.get(pk=pkv)

        heur = voyage.dateArrivee - voyage.dateDepert

        prix = utilisateur.nombreSiegeReserve * voyage.prix

        prix = prix/493

    paypal_dict = {
        "business": "zaenma.halidisalim@gmail.com",
        "amount": prix,
        "item_name": "Ticket de transport",
        "invoice": "unique-invoice-id",
        "currency_code": "EUR",
        "return": request.build_absolute_uri(reverse('achat:success', kwargs={'pkv': pkv, 'pku': pku, 'tag': tag, 'date': datetime.datetime.now()})),
        # "notify_url": request.build_absolute_uri(reverse('achat:success', kwargs={'pkv': request.GET['pkv'], 'pku': request.GET['pku'], 'tag': request.GET['tag'], 'date': datetime.datetime.now()})),
        "cancel_return": request.build_absolute_uri(reverse('paiement:paiement', kwargs={'pkv': pkv, 'tag': tag, 'pku': pku, 'date': datetime.datetime.now()})),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    
    form = PayPalPaymentsForm(initial=paypal_dict)

    donnees = {'user': utilisateur,
               'voyage': voyage, 'heur': heur, 
               'prix': prix, 'pkv': pkv, 'pku': pku, 
               'tag': tag, 'date': date, 'formPaypal': form}

    return render(request, 'paiement.html', donnees)
