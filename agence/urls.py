
from django.urls import path, include
from . import views

app_name = "agence"

urlpatterns = [
    path('<int:pk>', views.index, name='index-agence'),
]
