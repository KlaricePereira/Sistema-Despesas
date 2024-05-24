from django.db import models
from django.contrib.auth.models import User

class Saida(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Entrada(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo