from django.urls import path 
from . import views

# Definição das Urls que serão utilizadas para cada método criado
urlpatterns = [
    path('criar/', view=views.criar_usuario, name='criar_usuario'),
    path('logar/', view=views.logar_usuario, name='logar_usuario'), 
    path('read/', view=views.read, name='read'),
    path('criar/', view=views.criar, name='criar'),
    path('atualizar/<int:pk>', view=views.atualizar, name='atualizar'),
    path('deletar/<int:pk>', view=views.deletar, name='deletar'),
]