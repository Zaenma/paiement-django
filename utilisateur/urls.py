
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "infos"

urlpatterns = [
     path('<int:pkv>/<str:tag>', views.information, name='information'),
         
    path('<int:pkv>/<str:tag>/<str:msg>', views.information, name='erreur-abonnement'),

     path('password', views.reset_password, name='password'),

     path('dashbord', views.dashbord, name='dashbord'),

     path('dashbord/<str:action>', views.dashbord, name='dashbord'),
    
     path('dashbord/<str:action>/<str:element>', views.dashbord, name='dashbord'),

    #  path('dashbord/<str:agence>/', views.dashbord, name='dashbord'),
     

     path('', include('django.contrib.auth.urls')),

]
