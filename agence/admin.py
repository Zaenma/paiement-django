from django.contrib import admin

from .models import TypeAgence, Agence, AgenceAdmin

admin.site.register(TypeAgence)
admin.site.register(Agence, AgenceAdmin)
