from django.contrib import admin

from .models import Ile, Ville, VoyagesPrevu, VoyagesPrevuAdmin, IlsAdmin, VilleAdmin


admin.site.register(Ile, IlsAdmin)
admin.site.register(Ville, VilleAdmin)
admin.site.register(VoyagesPrevu, VoyagesPrevuAdmin)
