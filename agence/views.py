from django.shortcuts import render

# Create your views here.
from .formulaire import MessageForm
from .models import Agence


def index(request, destinateur=None):
    formulaire = MessageForm()
    agence = Agence.objects.get(pk=destinateur)
    donnees = {'destinateur': destinateur,
               'fmge': formulaire,
               'ag': agence,
               }
    return render(request, 'agence/index.html', donnees)
