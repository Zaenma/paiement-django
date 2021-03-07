from django.contrib import admin

# Register your models here.
from  .models import Contact, AdminContact


admin.site.register(Contact, AdminContact)