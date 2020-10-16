from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    primeiro_nome = forms.CharField()
    ultimo_nome = forms.CharField()
    email = forms.EmailField()
    data_aniversario = forms.DateField()
    codigo_area = forms.CharField()
    numero_telefone = forms.CharField()
    pais = forms.CharField()
    estado = forms.CharField()
    cidade = forms.CharField()

    class Meta:
        model = Cliente
        fields = (
            'primeiro_nome',
            'ultimo_nome',
            'email',
            'data_aniversario',
            'codigo_area',
            'numero_telefone',
            'pais',
            'estado',
            'cidade'
        )
