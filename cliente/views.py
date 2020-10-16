from django.shortcuts import render
from django.views.generic import ListView
from .models import Cliente


class ClienteListView(ListView):
    template_name = "cliente/cliente_list.html"
    model = Cliente
    queryset = Cliente.objects.all()

