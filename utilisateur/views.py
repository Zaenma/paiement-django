from django.shortcuts import render, redirect
from django.http import HttpResponse

from voyage_prevu.models import VoyagesPrevu
from utilisateur.formulaire import UtilisateurForm
from .models import Utilisateur
from agence.models import Agence


def index(request, pkv, pku=None):
    voyage = VoyagesPrevu.objects.get(id=pkv)
    agences = Agence.objects.all()

    if request.method == "POST":
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            return redirect('../paiement')
            # form.save()
        form = UtilisateurForm()
    else:
        form = UtilisateurForm()

    donnees = {'fu': form, 'voyage': voyage, 'ags': agences}

    return render(request, 'utilisateur/index.html', donnees)
