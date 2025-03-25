from django.urls import path
from . import views

# Define as urls que serão usadas para cada view
urlpatterns = [
 path('', views.lista_livros, name='lista_livros'),
 path('biblioteca/', views.criar_livros, name='criar_livros'),
 path('criarlivros/', views.criar_livros, name='criar_livros'),
 path('atualizar/<int:pk>/', views.atualizar_livros, name='atualizar_livros'), 
 path('deletar/<int:pk>/', views.deletar_livros, name='deletar_livros'),
 path('pesquisar/', views.busca_livros, name='buscar_livros')
]
