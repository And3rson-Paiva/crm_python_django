from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'primeiro_nome', 'ultimo_nome', 'email']



admin.site.register(Cliente, ClienteAdmin)