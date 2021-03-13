from django.contrib import admin
from .models import Achat, AdminAchat
# Register your models here.
admin.site.register(Achat, AdminAchat)
