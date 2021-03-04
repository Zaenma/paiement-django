from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
import datetime
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from agence.models import Agence
from voyages.models import VoyagesParAvion, VoyagesParBateau, VoyagesParBu, Ville, Ile
from .models import AbonnesMensuel
from .formulaire import UtilisateurForm, VoyagesParAvionForm, VilleForm, IleForm, VoyagesParBateauForm, AbonneForm


def information(request, pkv, tag=None):
    # Initialisation du formulaire
    formulaire = UtilisateurForm()

    #initiation du formulaire d'abonnement 
    formAbonnement = AbonneForm()

    erreurForm = None
    # Variable d'erreur
    erreur = 0

    if tag == 'AV':
        informationVoyage = VoyagesParAvion.objects.get(pk=pkv)

    if tag == 'BA':
        informationVoyage = VoyagesParBateau.objects.get(pk=pkv)

    if tag == 'BU':
        informationVoyage = VoyagesParBu.objects.get(pk=pkv)

    # Traitement du formulaire d'un nouveua utilisateur
    if request.method == "POST":
        formulaire = UtilisateurForm(request.POST)
        if request.POST["nom"] != request.POST["prenom"]:
            if int(request.POST["nombreSiegeReserve"]) >= 1:
                if formulaire.is_valid:
                    formulaire.save()
                    return HttpResponseRedirect(reverse('paiement:paiement', kwargs={'pkv': pkv, 'tag': tag, 'pku': request.POST["email"], 'date': datetime.datetime.now()}))
                else:
                    formulaire = UtilisateurForm(request.POST)
                    erreur = 1
            else:
                formulaire = UtilisateurForm(request.POST)
                erreur = 1
        else:
            formulaire = UtilisateurForm(request.POST)
            erreur = 1

        erreurForm = formulaire.errors.items()

    # Traitement de formulaire d'abonnement 
    if request.method == "GET":
        formAbonnement = AbonneForm(request.GET)

        if formAbonnement.is_valid:
            pass
            # abonne = AbonnesMensuel.objects.get(codeAbonnement__exact=request.GET["codeAbonnement"])
            # return HttpResponseRedirect(reverse('paiement:paiement', kwargs={'pkv': pkv, 'tag': tag, 'pku': abonnee., 'date': datetime.datetime.now()}))
        else:
            formulaire = AbonneForm(request.POST)
            erreur = 1

    donnees = {'infvoyage': informationVoyage,
               'form': formulaire,
               'erreur': erreur,
               'erf': erreurForm,
               'abf': formAbonnement
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


# vue de dashbord des administrateur des agences
def dashbord(request, action=None, element=None, formulaire=None, statut=None):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        donnees_agence = Agence.objects.get(responsable=request.user.username)
        
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
                nbreV = nombreVoyage(request, VoyagesParAvion)
                donneeaffiche = voyagesAffichees(request, VoyagesParAvion)
            else:
                pass

            donnees = {
                    'donnee': donneeaffiche,
                    # 'nbvg': nbreV,
                    'action': action,
                    'element': element,
                    'statut': statut,
                    'ag': donnees_agence,
                    }

        else:
            donnees = {'action': action,
                    'element': element,
                    'statut': statut, 
                    }

        donnees = {'nbvg': nombreVoyage(request), 'ag': donnees_agence,}
        return render(request, 'dashbord.html', donnees)


def reset_password(request):
    return render(request, 'registration/password_reset_form.html')


def logout(request):
    return render(request, 'registration/logged_out.html')
