from django.contrib import admin

# Register your models here.
from .models import Banque, StatistiqueVente, AdminBanque, AdminStatistique

admin.site.register(Banque, AdminBanque)
admin.site.register(StatistiqueVente, AdminStatistique)
