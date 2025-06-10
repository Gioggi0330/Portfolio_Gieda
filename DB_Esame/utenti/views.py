from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import authenticate, login, logout
from .models import Utente
from .serializers import UtenteSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@api_view(['POST'])
def registrazione(request):
    if request.method == 'POST':
        serializer = UtenteSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = request.data['password']
            nome = serializer.validated_data['nome']
            cognome = serializer.validated_data['cognome']
            user = Utente.objects.create_user(email=email, nome=nome, cognome=cognome, password=password)
            return JsonResponse({'message': 'Utente registrato con successo'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)  # Usa Token con la lettera maiuscola
        return Response({'token': token.key})
    else:
        return Response({'detail': 'Credenziali non valide'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_user(request):
    logout(request)
    return JsonResponse({'message': 'Logout avvenuto con successo'})

@api_view(['DELETE'])
def delete_account(request):
    if request.user.is_authenticated:
        request.user.delete()
        return JsonResponse({'message': 'Account cancellato con successo'})
    return JsonResponse({'error': 'Autenticazione richiesta'}, status=status.HTTP_400_BAD_REQUEST)
