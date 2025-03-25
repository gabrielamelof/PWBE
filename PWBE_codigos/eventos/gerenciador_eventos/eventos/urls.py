from django.urls import path
from . import views 


# Definição das Urls que serão utilizadas para cada método criado
urlpatterns = [
    path('eventos/', views.read_eventos),
    path('eventos/buscar/<int:pk>', views.pegar_evento),
    path('eventos/criar/', views.create_evento),
    path('eventos/atualizar/<int:pk>', views.update_evento),
    path('eventos/deletar/<int:pk>', views.delete_evento),
    path('eventos/futuros/', views.read_futuros),

]