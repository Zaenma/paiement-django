
from django.urls import path, include
from . import views

app_name = "achat"

urlpatterns = [
    path('', views.index, name='successs'),
    path('<int:pkv>/<str:pku>/<str:tag>/<str:date>', views.index, name='success'),
]
