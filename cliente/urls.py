from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView


app_name = "cliente"

urlpatterns = [
    path('lista/', ClienteListView.as_view(), name="cliente_list"),
    path('', ClienteCreateView.as_view(), name="criar_cliente"),
    path('<int:id>/', ClienteUpdateView.as_view(), name='cliente_update')

]
