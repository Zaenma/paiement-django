
from django.urls import path, include
from . import views

app_name = "paiement"

urlpatterns = [
    path('<int:pkv>/<str:tag>/<str:pku>/', views.paiement, name='paiement'),
    # path('<int:pkv>/<str:tag>/<str:pku>/<str:date>', views.paiement, name='paiement'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    
    # path('<int:pkv>/<str:tag>/<int:pku>',views.paiement, name='m_paiement'),
]
