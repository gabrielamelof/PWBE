from django.db import models

# Create your models here.

# Cria uma classe que define os campos a serem preenchidos pelo usuário
class Cadastro(models.Model):
 titulo = models.CharField(max_length=200)
 autor = models.CharField(max_length=200)
 ano_publicacao = models.CharField(max_length=4)


 def __str__(self):
    return self.titulo
 
 class Meta:
        verbose_name_plural = "Cadastros"
