from django.db import models

# Create your models here.

# Model que define os campos que o usuário preencherá 
class Tarefa(models.Model):
 status = models.CharField(max_length=11)
 descricao = models.TextField()
 data_criacao = models.DateTimeField(auto_now_add=True)
 

 def __str__(self):
    return self.status
