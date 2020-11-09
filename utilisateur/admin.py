from django.contrib import admin
from .models import Utilisateur, ResponsablesAgence, UtilisateurAdmin

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(ResponsablesAgence)
