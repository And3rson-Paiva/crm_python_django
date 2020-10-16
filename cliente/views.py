from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import Cliente
from .forms import ClienteForm


class ClienteCreateView(CreateView):
    template_name = 'cliente/cliente.html'
    form_class = ClienteForm

    def form_valid(self, form):
        return super().form_valid(form)


class ClienteListView(ListView):
    template_name = "cliente/cliente_list.html"
    model = Cliente
    queryset = Cliente.objects.all()

