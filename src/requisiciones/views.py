from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from requisiciones.models import *
from requisiciones.serializers import *

class RequisicionesViewSet(ViewSet):

    def list(self, request):
        queryset = Requisicion.objects.filter(usuario_creacion=request.user)
        serializer = RequisicionSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        requisicion = Requisicion(**request.data)
        requisicion.usuario_creacion = request.user
        requisicion.estatus = RequesicionEstatus.objects.get(id=RequesicionEstatus.EN_ESPERA)
        requisicion_estado = RequisicionEstado.objects.create(usuario_creacion=request.user)
        requisicion.estado = requisicion_estado
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
        requisicion.estatus_id = RequesicionEstatus.COTIZADO
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

    @action(detail=True, methods=['get','put'])
    def estados(self, request, pk=None):
        if request.method == 'PUT':
            requisicion = Requisicion.objects.select_related('estado').get(id=pk)
            requisicion.estatus_id = request.data['estatus_id']
            requisicion.save()
            requisicion.estado.categoria_id = request.data['categoria_id']
            requisicion.estado.razon = request.data['razon']
            requisicion.estado.save()
            return Response(status.HTTP_200_OK)
        else:
            requisicion = Requisicion.objects.get(id=pk)
            serializer = RequisicionEstadoSerializer(requisicion.estado)
            return Response(serializer.data, status.HTTP_200_OK)
            
    @action(detail=False, methods=['get'])
    def filtrados(self, request):
        queryset = Requisicion.objects.filter(estatus_id=RequesicionEstatus.ACEPTADO)
        serializer = RequisicionSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
 
    @action(detail=False, methods=['get'])   
    def filtrado_tipo(self, request):
        requisicion_tipo=request.GET.get('visible','')
        queryset = Requisicion.objects.filter(estatus_id=requisicion_tipo)
        serializer = RequisicionSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def cotizaciones_compras(self, request, pk=None):
        cotizacion_compras = CotizacionCompras(**self.request.data)
        cotizacion_compras.usuario_creacion = request.user
        cotizacion_compras.save()
        requisicion = Requisicion.objects.get(id=pk)
        requisicion.cotizacion_compras = cotizacion_compras
        requisicion.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def reportes(self, request, pk= None):
        queryset = ReporteCompras.objects.filter(requisicion_id=pk)
        serializer = ReporteComprasSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def create_reporte(self, request, pk=None):
        reporte = ReporteCompras(**self.request.data)
        reporte.usuario_creacion = request.user
        reporte.requisicion_id= pk
        reporte.estado_compra = EstatusCompras.objects.get(id=EstatusCompras.EN_ESPERA)
        reporte.save()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def create_compra_rapida(self, request, pk=None):
        compra_rapida. usuario_creacion = request.user
        compra_rapida.save()
        requisicion = Requisicion.objects.get(id=pk)
        requisicion.compra_rapida = compra_rapida
        requisicion.save()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def total_requisiciones(self, request):
        requisiciones_espera = len(list(Requisicion.objects.filter(estatus_id=RequesicionEstatus.EN_ESPERA)))
        requisiciones_cotizadas = len(list(Requisicion.objects.filter(estatus_id=RequesicionEstatus.COTIZADO)))
        requisiciones_aceptadas = len(list(Requisicion.objects.filter(estatus_id=RequesicionEstatus.ACEPTADO)))
        requisiciones_rechazadas = len(list(Requisicion.objects.filter(estatus_id=RequesicionEstatus.RECHAZADO)))
        # print(requisiciones_espera,requisiciones_cotizadas,requisiciones_aceptadas,requisiciones_rechazadas)
        
        data_requisiciones=[{"espera":requisiciones_espera,
        "cotizadas":requisiciones_cotizadas,
        "aceptadas":requisiciones_aceptadas,
        "rechazadas":requisiciones_rechazadas}]
        return Response(data_requisiciones, status.HTTP_200_OK)
