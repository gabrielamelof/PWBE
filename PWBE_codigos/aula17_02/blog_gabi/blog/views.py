from django.shortcuts import render
from .models import Postagem

# Create your views here.

#  View para listar todos os registros existentes por ordem decrescente de data de criação
def listar_postagens(request):
    postagens = Postagem.objects.all().order_by('-data_criacao')
    return render(request, 'blog/luana.html', {'postagens':postagens})
