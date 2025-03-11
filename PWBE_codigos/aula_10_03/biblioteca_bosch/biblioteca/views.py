from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadastro
from .forms import Itemform

# Create your views here.
def lista_livros(request):
    if request.method =="POST":
        livro = busca_livros(request)
        # return busca_livros(request)
    else:
        livro = []
    livros = Cadastro.objects.all()
    return render(request, 'biblioteca/lista_livros.html', {'livros' : livros, 'livro': livro})

def criar_livros(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = Itemform()
    return render(request, 'biblioteca/criar_livros.html', {'form' : form})


def atualizar_livros(request, pk):
    livro = get_object_or_404(Cadastro, pk=pk)
    if request.method == 'POST':
        form = Itemform(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else: 
        form = Itemform(instance=livro)
    return render(request, 'biblioteca/criar_livros.html', {'form' : form})

def deletar_livros(request, pk):
    livro = get_object_or_404(Cadastro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'biblioteca/excluir.html', {'livro' : livro})

def busca_livros(request):
    informacao = request.POST.get('info_livro')
    print(informacao)
    livro = Cadastro.objects.filter(ano_publicacao__icontains = informacao) | Cadastro.objects.filter(autor__icontains = informacao) | Cadastro.objects.filter(titulo__icontains = informacao)
    return livro
    # return render(request, 'biblioteca/lista_livros.html', {'livros' : livros2})