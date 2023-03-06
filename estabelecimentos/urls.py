from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.index, name = 'home'),
    path('cardapio', views.cardapio, name = 'cardapio'),
    path('contato', views.contato, name = 'contato'),
    path('listar_estabelecimento', views.listar_estabelecimento, name = 'listar_estabelecimento'),
    path('listar_mesa', views.listar_mesa, name = 'listar_mesa'),
    path('listar_garcom', views.listar_garcom, name = 'listar_garcom'),
    path('listar_cardapio', views.listar_cardapio, name = 'listar_cardapio')

]


# funciona em partes
#    path('lista_estabelecimentos', views.lista_estabelecimentos, name='lista_estabelecimentos'),
#    path('editar_estabelecimento/<int:estabelecimento_id>/', views.editar_estabelecimento, name='editar_estabelecimento'),



#from django.urls import path
#from .views import lista_estabelecimentos, editar_estabelecimento
#
#urlpatterns = [
#    path('estabelecimentos/', lista_estabelecimentos, name='lista_estabelecimentos'),
#    path('estabelecimentos/editar/<int:estabelecimento_id>/', editar_estabelecimento, name='editar_estabelecimento'),
#]

# Exemplo do Professor
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<int:aluno_id>', views.aluno, name='aluno')
#]