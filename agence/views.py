from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

# Create your views here.
from .formulaire import MessageForm, ConnexionForm
from .models import Agence


def index(request, destinateur=None):
    formulaire = MessageForm()
    agence = Agence.objects.get(pk=destinateur)
    donnees = {'destinateur': destinateur,
               'fmge': formulaire,
               'ag': agence,
               }
    return render(request, 'agence/index.html', donnees)

# page de connexion des agences

def formulaireConnexion(request, formulaire):
    if request.GET['adresseEmail'] and request.GET['mdp']:
        agence = Agence.objects.filter(
            Q(adresseEmail__exact=request.GET["adresseEmail"]) &
            Q(mdp__exact=request.GET["mdp"]))
        nombreAgence = agence.count()

        if nombreAgence.exist():
            return True

        # if nombreAgence == 1:
        #     return HttpResponseRedirect(reverse('infos:dashbord', kwargs={'agence': request.GET["adresseEmail"]}))

            # return agence.adresseEmail
    else:
        return False
    # formulaire = ConnexionForm()
    # if request.method == "GET":
    #     formulaire = ConnexionForm(request.GET)
    #     if formulaire.is_valid():
    #         agence = Agence.objects.filter(
    #             Q(adresseEmail__exact=request.GET["adresseEmail"]) &
    #             Q(mdp__exact=request.POST["mdp"]))
    #         agence.count()

    #         if agence == 1:
    #             return True
    #         else:
    #             return "autre chose"
    # else:
    #    return False

def connexion(request):
    formulaire = ConnexionForm()

    erreur = False

    # erreur = formulaireConnexion(request, formulaire)
    # agence = Agence.objects.all()


    # if request.method == "POST":
    #     messa = "Formulaire valide"

    #     formulaire = ConnexionForm(request.POST)
    #     if formulaire.is_valid():

            # agence = Agence.objects.filter(
            #     Q(adresseEmail__exact=request.POST["adresseEmail"]) &
            #     Q(mdp__exact=request.POST["mdp"]))

        #     agence = Agence.objects.filter(Q(adresseEmail__exact=request.POST["adresseEmail"]))
        #     donnees = {'agence': agence, 'erreur': erreur, 'm': messa}

        #     if agence != None:
        #         erreur = 1
        #     else:
        #         erreur = 0
        # else:
        #     erreur = 0

    donnees = {'formulaire': formulaire, 'erreur': erreur}
    return render(request, "agence/connexion.html", donnees)