from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu
from agence.models import Agence
from voyages.formulaire import AvionForm, BateauForm, BusForm
from django.shortcuts import render, redirect
import datetime
from .formulaire import ContactForm
from django.core.mail import send_mail
# Les imports de l'application

# Traitement du formulaire de contact
def formulaireContact(request, formulaire):
    if request.method == "POST":
        formulaire = ContactForm(request.POST)
        if formulaire.is_valid():
            email = formulaire.cleaned_data['email']
            sujet = formulaire.cleaned_data['sujet']
            message = '<b>Nom de l\'expéditeur : ' + formulaire.cleaned_data['nom'] + '</b> ' + '<br> <br>' + '<b> Téléphone : ' + formulaire.cleaned_data['telephone'] + '</b> </br> </br> Contenu du message : </br>' + formulaire.cleaned_data['message']
            destinateur = ['zaenma.halidisalim@gmail.com']
            if formulaire.save():
                # if send_mail(sujet, message, email, destinateur):
                return 1
        else:
            return 0

def index(request):
    # les formulaire de recherches
    avion = AvionForm()
    bateau = BateauForm()
    bus = BusForm()
    
    contactForm = ContactForm()

    heurbateau = VoyagesParBateau.objects.filter(
        dateArrivee__gte=datetime.date.today()).order_by('dateDepert')[:5]

    heuravion = VoyagesParAvion.objects.filter(
        dateArrivee__gte=datetime.date.today()).order_by('dateDepert')[:5]

    heurbus = VoyagesParBu.objects.filter(
        dateArrivee__gte=datetime.date.today()).order_by('dateDepert')[:5]
        
    agence = Agence.objects.all()

    statuscontact = formulaireContact(request, contactForm)

    # le dictionnaire à envoyer dans le template
    donnees = {'av': avion, 'ba': bateau, 'bu': bus,
               'agence': agence, 'heurbateau': heurbateau, 
               'heuravion': heuravion, 'heurbus': heurbus, 
               'cf': contactForm, 
               'statuscontact': statuscontact}

    return render(request, 'index.html', donnees)


