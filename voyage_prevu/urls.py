
from django.urls import path, include
from . import views

app_name = "voyage"

urlpatterns = [
    path('', views.index, name='index-voyage'),
    # path('recherche/', views.recherche, name='recherche'),
]
