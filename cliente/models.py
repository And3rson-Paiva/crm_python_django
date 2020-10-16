from django.db import models
from django.urls import reverse


class Cliente(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=50)
    email = models.EmailField()
    data_aniversario = models.DateField()
    codigo_area = models.CharField(max_length=3)
    numero_telefone = models.CharField(max_length=9)
    pais = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.primeiro_nome} {self.ultimo_nome}'

    def retorna_telefone(self):
        return f'({self.codigo_area}) {self.numero_telefone}'

    def retorna_nome_completo(self):
        return f'{self.primeiro_nome} {self.ultimo_nome}'

    def retorna_cidade_completa(self):
        return f'{self.estado} - {self.cidade}'

    def get_absolute_url(self):
        return reverse('cliente:cliente_update', kwargs={'id': self.id})
