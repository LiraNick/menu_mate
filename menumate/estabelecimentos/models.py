from django.db import models

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

class Mesa(models.Model):
    status_mesa = models.BooleanField()
    numero = models.IntegerField()
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

class Garcom(models.Model):
    nome = models.CharField(max_length=100)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data = models.DateTimeField()

class Menu(models.Model):
    nome = models.CharField(max_length=100)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
