from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.

from .models import Utilisateur, AdminUtilisateur, AbonnesAnnuel, AbonnesMensuel, AdminAbonnesAnnuel, AdminAbonnesMensuel, VersementsAbonneAnnuel, VersementsAbonneMensuel, AdminVersementsAbonneAnnuel, AdminVersementsAbonneMensuel, AbonnesHebdomadaire, AdminAbonnesHebdomadaire


admin.site.register(Utilisateur, AdminUtilisateur)
admin.site.register(AbonnesAnnuel, AdminAbonnesAnnuel)
admin.site.register(AbonnesMensuel, AdminAbonnesMensuel)
admin.site.register(AbonnesHebdomadaire, AdminAbonnesHebdomadaire)
admin.site.register(VersementsAbonneAnnuel, AdminVersementsAbonneAnnuel)
admin.site.register(VersementsAbonneMensuel, AdminVersementsAbonneMensuel)
