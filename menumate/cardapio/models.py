from django.db import models
from estabelecimentos.models import Menu

class ItemMenu(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
