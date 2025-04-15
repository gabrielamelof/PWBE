from rest_framework import serializers
from .models import Usuario

# Seializer utilizado para transformar as informações em JSON
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'