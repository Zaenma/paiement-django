from django.contrib import admin

# Mes imports
from .models import Ile, IlsAdmin, Ville, VilleAdmin, VoyagesParAvion, AdminVoyagesParAvion, VoyagesParBateau, AdminVoyageParBateau, VoyagesParBu, AdminVoyageParBus


admin.site.register(Ile, IlsAdmin)
admin.site.register(Ville, VilleAdmin)
admin.site.register(VoyagesParAvion, AdminVoyagesParAvion)
admin.site.register(VoyagesParBateau, AdminVoyageParBateau)
admin.site.register(VoyagesParBu, AdminVoyageParBus)
