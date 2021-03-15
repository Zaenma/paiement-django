from django.contrib import admin

# Register your models here.
from .models import Agence, AdminAgence, MessageAgence, AdminMessage, Reponse, AdminReponse, MessagesEnvoye, AdminMessageEnvoye

admin.site.register(Agence, AdminAgence)
admin.site.register(MessageAgence, AdminMessage)
admin.site.register(Reponse, AdminReponse)
admin.site.register(MessagesEnvoye, AdminMessageEnvoye)
