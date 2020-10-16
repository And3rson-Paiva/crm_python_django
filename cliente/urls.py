from django.urls import path
from .views import ClienteListView


app_name = "cliente"

urlpatterns = [
    path('lista/', ClienteListView.as_view(), name="cliente_list"),
]
