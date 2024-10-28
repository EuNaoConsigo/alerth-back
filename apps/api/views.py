from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import ClientSerializer, ClientLoginSerializer, Client
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from django.contrib.auth.hashers import make_password


# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    serializer = ClientLoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data  # O usuário foi retornado como objeto do modelo User

        # Gera os tokens para o usuário
        tokens = get_tokens_for_user(user)

        return Response({
            "message": "Login bem-sucedido!",
            "user": {
                "email": user.email,
                "username": user.username,
            },
            "tokens": tokens,
        })

    # Em caso de erro, retorne as mensagens de erro
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    # Checando se o email já está cadastrado
    if User.objects.filter(email=email).exists():
        return Response({"error": "Email já cadastrado."}, status=status.HTTP_400_BAD_REQUEST)

    # Criando o usuário
    user = User.objects.create(
        username=email,  # Pode usar o email como username
        email=email,
        password=make_password(password)  # Usando make_password para hashear a senha
    )

    client = Client.objects.create(
        name=name, 
        email=email)
    
    # Gerando tokens para o novo usuário
    tokens = get_tokens_for_user(user)

    client_data = ClientSerializer(client).data


    return Response({
        "message": "Usuário criado com sucesso!",
        "client": client_data,
        "user": user.username,
        "tokens": tokens
    }, status=status.HTTP_201_CREATED)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def test_token(request):
    return Response({"message": "Acesso liberado para {}".format(request.user.email)})