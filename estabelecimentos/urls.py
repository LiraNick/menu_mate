from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('configuracao', views.configuracoes, name='configuracao'),
    path('contato', views.contato, name='contato')

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