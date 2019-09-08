from rest_framework import serializers
from requisiciones.models import Requisicion, RequesicionTipo

class RequisicionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Requisicion
        fields = '__all__'
        depth = 1

class RequisicionTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequesicionTipo
        fields = '__all__'