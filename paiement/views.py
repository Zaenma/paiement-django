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

        prix_visa = prix * 1.2 * 100
        prix_visa_info = prix * 1.2

    if tag == 'BA':
        voyage = VoyagesParBateau.objects.get(pk=pkv)

        heur = voyage.dateArrivee - voyage.dateDepert

        prix = utilisateur.nombreSiegeReserve * voyage.prix

        prix = prix/493
        prix_visa = prix * 1.2 * 100
        prix_visa_info = prix * 1.2

    if tag == 'BU':
        voyage = VoyagesParBu.objects.get(pk=pkv)

        heur = voyage.dateArrivee - voyage.dateDepert

        prix = utilisateur.nombreSiegeReserve * voyage.prix

        prix = prix/493
        prix_visa = prix * 1.2 * 100
        prix_visa_info = prix * 1.2

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

    # Paiement avec stripe

    # def get_context_data(self, **kwargs): # new
    #     context = super().get_context_data(**kwargs)
    #     context['key'] = settings.STRIPE_PUBLISHABLE_KEY
    #     return context

    donnees = {'user': utilisateur,
               'voyage': voyage, 'heur': heur, 
               'prix': prix, 'pkv': pkv, 'pku': pku, 
               'tag': tag, 'date': date, 'formPaypal': form, 
               'prix_visa': prix_visa,
               'prix_visa_info': prix_visa_info,
               'key': settings.STRIPE_PUBLISHABLE_KEY}

    return render(request, 'paiement.html', donnees)
