
from django.urls import path, include
from . import views

app_name = "utilisateur"

urlpatterns = [
    path('<int:pkv>', views.index, name='index-utilisateur'),
    # path('<int:pkv>/<int:pku>', views.index, name='paiement'),
]
