from rest_framework import serializers
from requisiciones.models import Requisicion

class RequisicionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Requisicion
        fields = ["id", "fecha_correo", "nota", "usuario_creacion"]
