from django.db import models

# Create your models here.

# Model que define os campos que o usuário deve preencher
class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    qntRodas = models.PositiveBigIntegerField()
    ano = models.PositiveBigIntegerField()
    cor = models.CharField(max_length=255)
    escolhas_combustivel = (
        ('GASOLINA', 'Gasolina'),
        ('ETANOL', 'Etanol'),
        ('GNV', 'GNV'), 
        ('ELETRICO', 'Eletrico'),
        ('ALCOOL', 'Alcool'), 
        ('DIESEL', 'Diesel'), 
        ('FB', 'FeedBack'),
        )
    combustivel = models.CharField(max_length=9, choices=escolhas_combustivel)

    def __str__(self):
        return self.nome