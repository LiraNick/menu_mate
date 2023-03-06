from django.shortcuts import render, get_object_or_404, redirect
from .models import Estabelecimento
from .models import Menu, ItemMenu
#from .forms import EstabelecimentoForm


def index(request):

    return render(request,'base.html')


def home(request):

    return render(request,'base.html')


def contato(request):
    
    return render(request, 'contato.html')


def cardapio(request):
    # Recupera todos os objetos Menu do banco de dados onde o menu_id é 1.
    menus = Menu.objects.filter(menu_id = 1)
    # Recupera todos os objetos Menu do banco de dados.
    #item_menus = ItemMenu.objects.all()
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

    return render(request, 'cardapio.html', context)


def lista_estabelecimentos(request):
    estabelecimentos = Estabelecimento.objects.all()

    dados = {'estabelecimentos': estabelecimentos}

    return render(request, 'estabelecimento.html', dados)


def editar_estabelecimento(request, estabelecimento_id):
    estabelecimentos = get_object_or_404(Estabelecimento, pk=estabelecimento_id)

    exibir = {'estabelecimento': estabelecimentos}

    return render(request, 'editar_estabelecimento.html', exibir)


"""
    form = EstabelecimentoForm(request.POST or None, instance=estabelecimento)
    if form.is_valid():
        form.save()
        return redirect('lista_estabelecimentos')
    return render(request, 'editar_estabelecimento.html', {'form': form})

def aluno(request, aluno_id):
    alunos = get_object_or_404(Alunos, pk = aluno_id)

    aluno_a_exibir = {'aluno': alunos}

    return render(request,'aluno.html', aluno_a_exibir)
"""