from django.contrib import admin

from .models import ModePaiement, Paiement, Message

admin.site.register(ModePaiement)
admin.site.register(Paiement)
admin.site.register(Message)