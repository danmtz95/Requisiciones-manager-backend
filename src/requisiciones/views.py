from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from requisiciones.models import Requisicion, RequesicionTipo, RequesicionEstatus, Cotizacion, CategoriaEstado
from requisiciones.serializers import RequisicionSerializer, RequisicionTipoSerializer, RequesicionEstatusSerializer, CategoriaEstadoSerializer

class RequisicionesViewSet(ViewSet):

    def list(self, request):
        queryset = Requisicion.objects.all()
        serializer = RequisicionSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        requisicion = Requisicion(**request.data)
        requisicion.usuario_creacion = request.user
        requisicion.estatus = RequesicionEstatus.objects.get(id=RequesicionEstatus.EN_ESPERA)  
        requisicion.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def tipos(self, request):
        queryset = RequesicionTipo.objects.all()
        serializer = RequisicionTipoSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def cotizaciones(self, request, pk=None):
        cotizacion = Cotizacion(**self.request.data)
        cotizacion.usuario_creacion = request.user
        cotizacion.save()
        requisicion = Requisicion.objects.get(id=pk)
        requisicion.cotizacion = cotizacion
        requisicion.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def categorias(self, request):
        queryset = CategoriaEstado.objects.all()
        serializer = CategoriaEstadoSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def estatus(self, request):
        queryset = RequesicionEstatus.objects.all()
        serializer = RequesicionEstatusSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
