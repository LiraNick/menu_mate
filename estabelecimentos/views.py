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

    item_menus = ItemMenu.objects.all()

    cardapio = {'item_menus': item_menus}

    return render(request, 'cardapio.html', cardapio)


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