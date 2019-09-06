from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

class ClientesViewSet(ViewSet):

    def list(self, request):
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)