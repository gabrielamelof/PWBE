from rest_framework import serializers
from .models import Carro

# Serializer usado para transformar as informações de JSON para modelo e modelo para JSON
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'