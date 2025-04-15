from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    biografia = models.CharField(max_length=255, null=True, blank=True)
    idade = models.PositiveBigIntegerField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    animais = models.IntegerField(null=True, blank=True)

    # Campo com escolhas pré-definidas para o usuário  
    escolhas_escolaridade = (
        ('ENSINO MÉDIO COMPLETO', 'Ensino Médio Completo'),
        ('GRAU SUPERIOR', 'Grau Superior'),
        ('ENSINO FUNDAMENTAL', 'Ensino Fundamental'), 
        )
    escolaridade = models.CharField(max_length=30, choices=escolhas_escolaridade, blank=True, null=True)

    #Define campos que não podem ser deixados em branco pelo usuário   
    REQUIRED_FIELDS = ['telefone', 'idade']

    def __str__(self):
        return self.username

