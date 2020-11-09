
from django.urls import path, include
from . import views

app_name = "paiement"

urlpatterns = [
    path('<int:pkv>', views.index, name='index-paiement'),
    path('<int:pkv>/<int:pku>', views.index, name='paiement'),
]
