
from django.urls import path
from . import views

app_name = "voyages"

urlpatterns = [
    path('', views.voyages, name='voyages'),
]
