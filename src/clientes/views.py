from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente

class ClientesViewSet(ViewSet):

    def list(self, request):
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        cliente = Cliente(**request.data)
        cliente.usuario_creacion = request.user
        cliente.save() 
        return Response(status=status.HTTP_200_OK)