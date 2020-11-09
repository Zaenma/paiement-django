from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
import datetime
from django.utils import timezone
from django.contrib.sessions.models import Session
from http import cookies


from voyage_prevu.models import VoyagesPrevu
from utilisateur.models import Utilisateur
from utilisateur.formulaire import UtilisateurForm
from agence.models import Agence


def index(request, pkv):
    voyage = VoyagesPrevu.objects.get(id=pkv)
    agences = Agence.objects.all()

    # Traitement du formulaire
    if request.method == "POST":
        form = UtilisateurForm(request.POST)
        if int(request.POST["age"]) < 100:
            if int(request.POST["age"]) > 15:
                if form.is_valid():
                    form.save()
                else:
                    form = UtilisateurForm()
            else:
                form = UtilisateurForm()
        else:
            form = UtilisateurForm()
    else:
        form = UtilisateurForm()

    # on selectionne la dernière date inseré dans la base de données
    utilisateur = Utilisateur.objects.latest('created_at')
    # on récupère aussi la date locale de l'appareil
    dernier_date = utilisateur.created_at
    # on ajoute 5 minutes à la date local
    date_local = timezone.now() + datetime.timedelta(minutes=5)
    # on compare si la dernière date inseré est superieur à la date local + 5 minutes, (voir la suite)
    if dernier_date > date_local:
        session = True
    else:
        session = False

    donnees = {'vp': voyage, 'fu': form, 'ags': agences,
               'su': utilisateur, 'session': session}

    return render(request, 'paiement/index.html', donnees)
