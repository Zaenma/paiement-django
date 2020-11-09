
from django.urls import path, include
from . import views

app_name = "accueil"

urlpatterns = [
    path('', views.index, name='index'),
    path('recherche/', views.recherche, name='recherche'),
]
