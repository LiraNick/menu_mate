from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .models import Mesa
from .models import Garcom
from .models import Cardapio
from .models import Categoria



def index(request):
    # Recupera todos os objetos Menu do banco de dados.
    mesas = Mesa.objects.all()
    garcons = Garcom.objects.all()
    itens_de_cardapio = Cardapio.objects.all()
    # 'Chave' : Valor, no HTML usar o nome da chave para o laço FOR
    context = {
        'mesas': mesas,
        'garcons': garcons,
        'itens_de_cardapio': itens_de_cardapio,
        }

    return render(request,'principal.html', context)