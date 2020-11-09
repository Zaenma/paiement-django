from django.shortcuts import render
from django.core.paginator import Paginator


from .models import VoyagesPrevu
from agence.models import Agence


def index(request):
    agences = Agence.objects.all()
    voyagesPrevu = VoyagesPrevu.objects.all()
    pagination = Paginator(voyagesPrevu, 5)
    nombre_page = request.GET.get('page')
    voyagesPrevu = pagination.get_page(nombre_page)
    donnees = {'vps': voyagesPrevu, 'ags': agences}
    return render(request, 'voyage_prevu/index-prevu.html', donnees)
