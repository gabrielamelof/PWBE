from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import	Usuario
from .serializers import UsuarioSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# view para o usuário criar um novo registro no banco de dados
@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    biografia = request.data.get('biografia')
    animais = request.data.get('animais')
    escolaridade = request.data.get('escolaridade')

    if not username or not senha or not idade or not telefone:
        return Response({'Erro': 'Campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST)

    if Usuario.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(username=username).exists():
        return Response({'Erro': f'usuário {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = Usuario.objects.create_user(
        username=username, 
        senha = senha, 
        telefone = telefone,
        endereco = endereco, 
        idade = idade, 
        biografia = biografia, 
        animais = animais, 
        escolaridade = escolaridade, 
    )
    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

# View usada para a autenticação de um usuário no banco de dados
@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')

    usuario = authenticate(username=username, password=senha)

    if usuario:
        refresh = RefreshToken.for_user(usuario)

        return Response({
            'Acesso': str(refresh.access_token), 
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuário e/ou senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)

# View para listagem de todos os registros cadatrados no banco de dados 
# Só pode ser usada se o usuário estiver autenticado
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read(request):
    usuarios = Usuario.objects.all() 
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#  View para criar um novo usuário
# Só pode ser usada se o usuário estiver autenticado
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# View para atualizar um usuário pelo seu id
# Só pode ser usada se o usuário estiver autenticado
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def atualizar(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'erro':'Usuario não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View para deletar um usuário pelo seu id
# Só pode ser usada se o usuário estiver autenticado
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletar(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'Erro':'Usuário não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    return Response({'Mensagem': f"O usuario: {usuario.username} foi excluido"}, status=status.HTTP_200_OK)