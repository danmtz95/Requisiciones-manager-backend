from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from proveedores.models import Proveedor
from proveedores.serializers import ProveedorSerializer


class ProveedoresViewSet(ViewSet):

    def list(self, request):
        queryset = Proveedor.objects.all()
        serializer = ProveedorSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        proveedor = Proveedor(**request.data)
        proveedor.usuario_creacion = request.user
        proveedor.save() 
        return Response(status=status.HTTP_200_OK)