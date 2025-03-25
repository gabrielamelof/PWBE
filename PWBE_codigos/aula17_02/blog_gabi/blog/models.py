from django.db import models

# Create your models here.

# Model que define os campos que o usuário preencherá
class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
