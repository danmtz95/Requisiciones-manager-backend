from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cliente
        fields = ['id', 'nombre', 'rfc', 'telefono', 'correo', 'usuario_creacion']
        read_only_fields = ["id"]
