from django.shortcuts import render
from .models import Agence


def index(request, pk):
    toute_agence = Agence.objects.all()
    agence = Agence.objects.get(id=pk)
    donnees = {'agence': agence, 'ags': toute_agence}
    return render(request, 'agence/index.html', donnees)
