from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.forms import formset_factory
from datetime import datetime 
from time import strftime
from django.db.models import Q, Sum, Avg
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from agence.models import Agence, MessagesEnvoye
from agence.formulaire import MessageEnvoyeForm
from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu, Ville, Ile
from .models import AbonnesMensuel, AbonnesAnnuel, AbonnesHebdomadaire
from .formulaire import UtilisateurForm, VoyagesParAvionForm, VilleForm, IleForm, VoyagesParBateauForm, AbonneForm
from achat.models import Achat
from django.core.mail import BadHeaderError, send_mail
# from django.db.models import Sum

# Traitement de formulaire d'abonnement 
def abonnement(request, pkv, tag=None):
    if request.method == "GET":
        if AbonneForm(request.GET).is_valid:
            if AbonnesMensuel.objects.filter(codeAbonnement=request.GET["codeAbonnement"]).exists():
                return AbonnesMensuel.objects.filter(codeAbonnement=request.GET["codeAbonnement"])
            elif AbonnesAnnuel.objects.filter(codeAbonnement=request.GET["codeAbonnement"]).exists():
                return AbonnesAnnuel.objects.filter(codeAbonnement=request.GET["codeAbonnement"])
            elif AbonnesHebdomadaire.objects.filter(codeAbonnement=request.GET["codeAbonnement"]).exists():
                return AbonnesHebdomadaire.objects.filter(codeAbonnement=request.GET["codeAbonnement"])
            else:
                return None
        else:
            return AbonneForm
            
def informationPersonnelles(request, formulaire):
    erreur = 1
    if request.method == "POST":
        formulaire = UtilisateurForm(request.POST)
        if request.POST["nom"] != request.POST["prenom"]:
            if int(request.POST["nombreSiegeReserve"]) >= 1:
                if formulaire.is_valid:
                    formulaire.save()
                    return HttpResponseRedirect(reverse('paiement:paiement', kwargs={'pkv': pkv, 'tag': tag, 'pku': request.POST["email"]}))
                else:
                    # formulaire = UtilisateurForm(request.POST)
                    return erreur
            else:
                # formulaire = UtilisateurForm(request.POST)
                return erreur
        else:
            # formulaire = UtilisateurForm(request.POST)
            return erreur

def information(request, pkv, tag=None, msg=None):
    # Initialisation du formulaire
    # formulaire = UtilisateurForm()

    #initiation du formulaire d'abonnement 
    formAbonnement = AbonneForm()

    if tag == 'AV':
        informationVoyage = VoyagesParAvion.objects.get(pk=pkv)

    elif tag == 'BA':
        informationVoyage = VoyagesParBateau.objects.get(pk=pkv)

    elif tag == 'BU':
        informationVoyage = VoyagesParBu.objects.get(pk=pkv)
    else:
        return render(request, 'erreur.html')
        
    # Traitement du formulaire d'un nouveua utilisateur
    # Utilisation des formulaire groupés
    formulaire = UtilisateurForm()
    
    erreur = informationPersonnelles(request, formulaire)

    if request.GET.get("codeAbonnement") != None:
        if abonnement(request, pkv, tag):
            variable_get = {'pkv': pkv, 'tag': tag, 'pku': request.GET['codeAbonnement']}
            return HttpResponseRedirect(reverse('paiement:paiement', kwargs=variable_get))
        elif abonnement(request, pkv, tag) == None:
            msg = 1
            HttpResponseRedirect(reverse('infos:erreur-abonnement', kwargs={'pkv': pkv, 'tag': tag, 'msg': msg}))
        
    donnees = {'infvoyage': informationVoyage,
               'form': formulaire,
               'erreur': erreur,
               'abf': formAbonnement,
               'data': request.GET
               }

    return render(request, 'information.html', donnees)

def formulaireAffiche(request, formulaire):
    if request.method == "POST":
        formulaire = VilleForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
            return 1
        else:
            return 0

# fonction de pagination -----------------------
def donneeAffichees(request, modelaffichee):
    lite = modelaffichee.objects.all()
    pagination = Paginator(lite, 5)
    nombre_page = request.GET.get('p')
    donneeaffiche = pagination.get_page(nombre_page)

    return donneeaffiche

# fonction de pagination -----------------------
def voyagesAffichees(request, modelaffichee):

    # on prend l'agence à laquelle le reponsabe de l'agence et la personne qui est connecté 
    donnees_agence = Agence.objects.get(responsable=request.user.username)
    
    # on prend les données dans l'une des tables des voyages à condition que le nom de l'agence 
    # est le même que celui qu'on a préalablement récupéré 
    lite = modelaffichee.objects.filter(agencePrincipal=donnees_agence.nom)

    pagination = Paginator(lite, 5)

    nombre_page = request.GET.get('p')

    voyagesaffiche = pagination.get_page(nombre_page)

    return voyagesaffiche

# calcule le nombre de voyage par agence 
def nombreVoyage(request):

    # on prend l'agence à laquelle le reponsabe de l'agence et la personne qui est connecté 
    donnees_agence = Agence.objects.get(responsable=request.user.username)
    
    # on prend les données dans l'une des tables des voyages à condition que le nom de l'agence 
    # est le même que celui qu'on a préalablement récupéré 
    
    nbv = VoyagesParAvion.objects.filter(agencePrincipal=donnees_agence.nom).count() + VoyagesParBateau.objects.filter(agencePrincipal=donnees_agence.nom).count() + VoyagesParBu.objects.filter(agencePrincipal=donnees_agence.nom).count()
    return nbv

# Nombre de ticket vendu
def ticketvendu(request):
    # on prend l'agence à laquelle le reponsabe de l'agence et la personne qui est connecté 
    donnees_agence = Agence.objects.get(responsable=request.user.username)
    # on prend les données dans l'une des tables des voyages à condition que le nom de l'agence 
    # est le même que celui qu'on a préalablement récupéré 
    nombreticketvendu = Achat.objects.filter(agence=donnees_agence.nom).count()

    return nombreticketvendu

def calculePourcentage(request):
     # on prend l'agence à laquelle le reponsabe de l'agence et la personne qui est connecté 
    donnees_agence = Agence.objects.get(responsable=request.user.username)
    # on prend les données dans l'une des tables des voyages à condition que le nom de l'agence 
    # est le même que celui qu'on a préalablement récupéré 
    voyage = VoyagesParAvion.objects.filter(agencePrincipal=donnees_agence.nom)
    pourcentage = (3/8)*100
    # totalsiege = voyage.annotate(Sum(nombreSiege))
    # totalsiege = voyage.codeVoyage
    return pourcentage
    
def formulaireEnvoieMessage(request):
    if request.method == "POST":
        formulairemessage = MessageEnvoyeForm(request.POST)
        if formulairemessage.is_valid():
            sujet = request.POST['sujet']
            email = request.POST['email']
            message = request.POST['message']
            agence = Agence.objects.get(responsable=request.user.username).nom
            if MessagesEnvoye.objects.create(agence=agence, email=email, sujet=sujet, message=message):
        
                # à decomenter lors du déploiement
                # send_mail(sujet, message, 'contact.zaenma@gmail.Com', [email, 'zaenma.halidisalim@gmil.com'])
                
                return 1
            else:
                return 0

# vue de dashbord des administrateur des agences
def dashbord(request, action=None, element=None, formulaire=None, statut=None):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        donnees_agence = Agence.objects.get(responsable=request.user.username)
        nbreV = nombreVoyage(request)

        nombreticketvendu = ticketvendu(request)

        if action == "ajout":
            if element == "ile":
                formulaire = IleForm()
                statut = formulaireAffiche(request, formulaire)

            elif element == "ville":
                formulaire = VilleForm()
                statut = formulaireAffiche(request, formulaire)

            elif element == "aerien":
                formulaire = VoyagesParAvionForm()
                statut = formulaireAffiche(request, formulaire)

            elif element == "maritime":
                formulaire = VoyagesParBateauForm()
                statut = formulaireAffiche(request, formulaire)

            elif element == "terrestre":
                formulaire = VoyagesParBateauForm()
                statut = formulaireAffiche(request, formulaire)

            else:
                pass

            donnees = {'form': formulaire,
                    'action': action,
                    'element': element,
                    'statut': statut,
                    'ag': donnees_agence,
                    }

        elif action == "affiche":
            if element == 'ile':
                donneeaffiche = donneeAffichees(request, Ile)

            elif element == 'ville':
                donneeaffiche = donneeAffichees(request, Ville)

            elif element == 'maritime':
                donneeaffiche = voyagesAffichees(request, VoyagesParBateau)

            elif element == 'terreste':
                donneeaffiche = voyagesAffichees(request, VoyagesParBu)

            elif element == 'aerien':
            
                donneeaffiche = voyagesAffichees(request, VoyagesParAvion)
            else:
                pass
            donnees = {
                    'donnee': donneeaffiche,
                    'nbvg': nbreV,
                    'action': action,
                    'element': element,
                    'statut': statut,
                    'ag': donnees_agence,
                    'nombreticketvendu': nombreticketvendu,
                    }

        elif action == "place-restant":
            bu = voyagesAffichees(request, VoyagesParBu)
            ba = voyagesAffichees(request, VoyagesParBateau)
            av = voyagesAffichees(request, VoyagesParAvion)

            donnees = {
                    'nbvg': nbreV,
                    'action': action,
                    'bu': bu,
                    'ba': ba,
                    'av': av,
                    'ag': donnees_agence,
                    'nombreticketvendu': nombreticketvendu,
                    }

        else:
            reponsemessage = formulaireEnvoieMessage(request)
            donnees = {'action': action,
                    'element': element,
                    'nbvg': nbreV,
                    'nombreticketvendu': nombreticketvendu,
                    'statut': statut,
                    'ag': donnees_agence,
                    'pc': calculePourcentage(request),
                    'fm': MessageEnvoyeForm(),
                    'rm': reponsemessage,
                    }

        return render(request, 'dashbord.html', donnees)


def reset_password(request):
    return render(request, 'registration/password_reset_form.html')


def logout(request):
    return render(request, 'registration/logged_out.html')
