from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contato
from .serializer import ContatoSerializer   

def index(request):
    return render(request, 'index.html')

# Criar Endpoints 
@api_view(['POST'])
def inserirContato(request):
    serializer = ContatoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarContatos(request):
    contatos = Contato.objects.all()
    serializer = ContatoSerializer(contatos, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizarContato(request, pk):
    try:
        contato = Contato.objects.get(id = pk)
    except Contato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ContatoSerializer(contato, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletarContato(request, pk):
    try:
        contato = Contato.objects.get(id = pk)
        contato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Contato.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
