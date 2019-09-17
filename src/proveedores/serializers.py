from rest_framework import serializers
from proveedores.models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Proveedor
        fields = ['id', 'nombre_fiscal','direccion','nombre_comercial', 'rfc', 'telefono', 'correo', 'usuario_creacion']
        read_only_fields = ["id"]
