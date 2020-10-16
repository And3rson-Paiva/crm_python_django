from django import forms
from .models import Cliente

class DateInput(forms.DateInput):
    input_type = 'date'


class ClienteForm(forms.ModelForm):
    primeiro_nome = forms.CharField(
        label='Nome',
        error_messages={'max_length': 'Nome não pode ter mais de 30 caracteres'}
    )
    ultimo_nome = forms.CharField(
        label='Sobrenome',
        error_messages={'max_length': 'Sobrenome não pode ter mais de '}
    )
    email = forms.EmailField(label='E-mail')
    data_aniversario = forms.DateField(label='Data de nascimento', widget=DateInput())
    codigo_area = forms.RegexField(
        label='DDD',
        regex=r'^\+?1?[0-9]{2}$',
        error_messages={'invalid': 'Número de DDD inválido'}
    )
    numero_telefone = forms.RegexField(
        label='Telefone',
        regex=r'^\+?1?[0-9]{9,15}$',
        error_messages={'invalid': 'Número de telefone inválido'}
    )
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
