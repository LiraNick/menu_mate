from django.shortcuts import render, get_object_or_404, redirect
from .models import Estabelecimento
from .models import Mesa
from .models import Garcom
from .models import Menu, ItemMenu
from .forms import EstabelecimentoForm


#-- -----------------------------------------------------
#-- Nav Menu
#-- -----------------------------------------------------
def index(request):

    return render(request,'base.html')


def home(request):

    return render(request,'base.html')


def contato(request):

    return render(request, 'contato.html')


#-- -----------------------------------------------------
#-- Estabelecimento
#-- -----------------------------------------------------
def listar_estabelecimento(request):
    # Recupera todo o objeto Menu do banco de dados onde o menu_id é 1.
    estabelecimentos = Estabelecimento.objects.filter(estabelecimento_id = 1)
    # 'Chave' : Valor, no HTML usar o nome da chave para o laço FOR
    lista_est = {'estabelecimentos': estabelecimentos}

    return render(request, 'estabelecimento.html', lista_est)


#def estabelecimento_form(request):
#    form = Estabelecimento()
#    return render(request, 'estabelecimento_form.html', {'form': form})


def estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estabelecimento')
    else:
        form = EstabelecimentoForm()
    return render(request, 'estabelecimento.html', {'form': form})


#-- -----------------------------------------------------
#-- Mesa
#-- -----------------------------------------------------
def listar_mesa(request):
    # Recupera todos os objetos Menu do banco de dados.
    mesas = Mesa.objects.all()

    lista_de_mesa = {'mesas': mesas}

    return render(request,'mesa.html', lista_de_mesa)


#-- -----------------------------------------------------
#-- Garçom
#-- -----------------------------------------------------
def listar_garcom(request):
    # Recupera todos os objetos Menu do banco de dados.
    garcons = Garcom.objects.all()

    lista_de_garcom = {'garcons': garcons}

    return render(request,'garcom.html', lista_de_garcom)



#-- -----------------------------------------------------
#-- Cardápio
#-- -----------------------------------------------------
def cardapio(request):
    # Recupera todo o objeto Menu do banco de dados onde o menu_id é 1.
    menus = Menu.objects.filter(menu_id = 1)
    # Recupera todos os objetos ItemMenu do banco de dados que pertencem à categoria especificada
    item_menus_lanche = ItemMenu.objects.filter(item_menu_categoria = 'Lanche')
    item_menus_bebidas = ItemMenu.objects.filter(item_menu_categoria = 'Bebida')
    item_menus_pastel = ItemMenu.objects.filter(item_menu_categoria = 'Pastel')

    # Dicionário contento as variávies.
    context = {
        'menus': menus,
        'item_menus_lanche': item_menus_lanche,
        'item_menus_bebidas': item_menus_bebidas,
        'item_menus_pastel': item_menus_pastel
    }

    return render(request, 'cardapio_home.html', context)


def listar_cardapio(request):
    # Recupera todos os objetos Menu do banco de dados.
    garcons = Garcom.objects.all()

    item_menus_lanche = ItemMenu.objects.filter(item_menu_categoria = 'Lanche')
    item_menus_bebidas = ItemMenu.objects.filter(item_menu_categoria = 'Bebida')
    item_menus_pastel = ItemMenu.objects.filter(item_menu_categoria = 'Pastel')

    # Dicionário contento as variávies.
    context = {
        'item_menus_lanche': item_menus_lanche,
        'item_menus_bebidas': item_menus_bebidas,
        'item_menus_pastel': item_menus_pastel
    }

    return render(request, 'cardapio.html', context)


"""
    form = EstabelecimentoForm(request.POST or None, instance=estabelecimento)
    if form.is_valid():
        form.save()
        return redirect('lista_estabelecimentos')
    return render(request, 'editar_estabelecimento.html', {'form': form})
"""