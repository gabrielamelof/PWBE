from rest_framework import serializers
from .models import Evento

# Seializer utilizado para transformar as informações em JSON
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'