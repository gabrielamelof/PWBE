from django.shortcuts import render
from .models import Tarefa

# Create your views here.

# View para listar todas as tarefas em ordem decrescente
def lista_tarefas(request):
 tarefas = Tarefa.objects.all().order_by('-data_criacao')
 return render(request, 'lista/lista_tarefas.html', {'tarefas': tarefas})