from rest_framework import serializers
from django.contrib.auth.models import User,Group

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        exclude = ('password', )

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
