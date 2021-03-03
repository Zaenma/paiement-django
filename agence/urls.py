from django.urls import path
from . import views

app_name = "agence"

urlpatterns = [
    path('<int:destinateur>', views.index, name='agence'),
    path('page-connexion', views.connexion, name='agence-connexion'),
]
