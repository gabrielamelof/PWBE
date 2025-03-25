from django.shortcuts import render
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta


# Create your views here.

# View para ler todos os eventos cadastrados
@api_view(['GET'])

def read_eventos(request):
    
    # Define os parâmetros passados para cada tipo de filtragem
    eventos = Evento.objects.all() 
    categoria = request.query_params.get('categoria')
    data = request.query_params.get('data')
    quantidade = request.query_params.get('quantidade')
    ordenar = request.query_params.get('ordenar')

    try:
        # Filtra os eventos por uma categoria que é passada como parâmetro
        if categoria:
            eventos = eventos.filter(categoria__icontains=categoria)
        
        # Filtra os eventos por uma data que é passada como parâmetro
        if data:
            eventos = eventos.filter(data__icontains=data)

        # Filtra os eventos por uma quantidade que é passada como parâmetro
        if quantidade: 
            eventos = eventos[:int(quantidade)]
        
        # Ordena os eventos pelas suas datas, da menor para a maior 
        if ordenar:
            eventos = eventos.order_by('data').values()

        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)
    
    except Evento.DoesNotExist:
        return Response({'erro':'Evento não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
     
   


@api_view(['GET'])

def read_futuros(request):
    eventos = Evento.objects.all() 
    # Pega dias como parâmetro e caso o usuário não passe um parâmtero, define como 7 dias
    dias = request.query_params.get('dias', '7')
    hoje = datetime.now()
    # Soma o dia de hoje com mais sete dias
    tempo_futuro = hoje + timedelta(days=int(dias))

    # Filtra os eventos para o período de tempo definido
    if dias:
        eventos = eventos.filter(data__gte=hoje, data__lte=tempo_futuro)

    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)


# View para buscar um evento pelo seu id
@api_view(['GET'])

def pegar_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro':'Evento não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento)
    return  Response(serializer.data)


#  View para criar um novo evento
@api_view(['POST'])

def create_evento(request):
    if request.method == 'POST':
        serializer = EventoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# View para atualizar um evento pelo seu id
@api_view(['PUT'])
def update_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro':'Evento não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View para deletar um evento pelo seu id
@api_view(['DELETE'])
def delete_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro':'Evento não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
    evento.delete()
    return Response({'Mensagem': f"O evento: {evento.nome} foi apagado"}, status=status.HTTP_200_OK)
    