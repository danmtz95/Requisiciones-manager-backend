from rest_framework import serializers
from requisiciones.models import Requisicion, RequesicionTipo, CategoriaEstado, RequesicionEstatus, RequisicionEstado, ReporteCompras

class RequisicionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Requisicion
        fields = '__all__'
        depth = 1

class RequisicionTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequesicionTipo
        fields = '__all__'

class CategoriaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaEstado
        fields = '__all__'

class  RequesicionEstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequesicionEstatus
        fields = '__all__'

class RequisicionEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisicionEstado
        fields = '__all__'

class ReporteComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteCompras
        fields = '__all__'