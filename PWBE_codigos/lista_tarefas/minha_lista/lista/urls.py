from django.urls import path
from . import views

# Define as urls das views
urlpatterns = [
 path('', views.lista_tarefas, name='lista_tarefas'),
]