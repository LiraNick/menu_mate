from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Estabelecimento



class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['estabelecimento_id','estabelecimento_nome', 'estabelecimento_endereco', 'estabelecimento_telefone']
        labels = {
            'estabelecimento_id' : ('Id'),
            'estabelecimento_nome' : ('Nome'),
            'estabelecimento_endereco' : ('Endereço'),
            'estabelecimento_telefone' : ('Telefone'),
        }



"""
Pergunta

Gostaria de saber, como abrir um formulário cujos campos já estejam previamente preenchidos
com os dados do usuário(resultantes de uma pesquisa no banco de dados), ficando a cargo
dele somente editar as informações.

Estou utilizando Django para programar, consegui fazer o formulário, porém não consigo recuperar ele pra edição.

Eu até consigo utilizando a função {{ form.as_p }}, porém eu gostaria de recuperar esses dados utilizando <input>, tem como?

Atualmente minha view para editar está da seguinte forma:

def editar(request, pk): # Funcao para editar um aluno
post = get_object_or_404(Aluno, pk=pk)
if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('aluno:detalhes', pk=post.pk)
else:
    form = PostForm(instance=post)
return render(request, 'aluno/editar.html', {'form': form})
E no html está assim:

  <form method="POST" class="post-form">{% csrf_token %}
                        <!--Entrada do nome do aluno-->
                        <label class="campos" for="nome">Nome:</label><br>
                        <input type="text" name="nome" id="nome" required autofocus >
                        <p></p>

Resposta 1
Para preencher manualmente o valor das tags de input no seu form você precisa referenciar os campos do formulário Django, pegar o .value deles e preencher no value do input, como no exemplo abaixo:

<input type="text" name="nome" id="nome" value="{{ form.nome.value|default:"" }}" required autofocus>
{# Tome nota para a tag "default" que é útil quando o campo está vazio pois em alguns casos ele ficaria mostrando o campo nulo "None" do Python #}

Resposta 2
Na sua view, na hora de instanciar o form, acrescente a instancia do objeto desejado.

meu_objeto = MyObject.objects.get(pk=meu_id)
form = MyForm(instance=meu_objeto)

"""