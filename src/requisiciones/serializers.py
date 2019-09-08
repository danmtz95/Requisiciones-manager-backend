from rest_framework import serializers
from requisiciones.models import Requisicion

class RequisicionSerializer(serializers.ModelSerializer):


    class Meta: 
        model = Requisicion
        fields = '__all__'
        depth = 0
