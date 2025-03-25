from django.db import models

# Create your models here.

# Classe que define os campos que serão pedidos na criação de um evento
class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField()
    # Blank = permite que o usuário não insira um valor
    local = models.CharField(max_length=255, blank=True)
    escolhas_categoria = (
        ('MÚSICA', 'Música'),
        ('PALESTRA', 'Palestra'),
        ('WORKSHOP', 'Workshop'), 
        )
    categoria = models.CharField(max_length=20, choices=escolhas_categoria, blank=True)

    def __str__(self):
        return self.nome