from django import forms
from .models import Cliente

class DateInput(forms.DateInput):
    input_type = 'date'


class ClienteForm(forms.ModelForm):
    primeiro_nome = forms.CharField(label='Nome')
    ultimo_nome = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='E-mail')
    data_aniversario = forms.DateField(label='Data de nascimento', widget=DateInput())
    codigo_area = forms.CharField(label='DDD')
    numero_telefone = forms.CharField(label='Telefone')
    pais = forms.CharField(label='País')
    estado = forms.CharField(label='Estado')
    cidade = forms.CharField(label='Cidade')

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
