from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Etiqueta

class EtiquetaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    titulo= serializers.CharField(max_length=25)
    descricao = serializers.CharField(max_length=75)   

    def create(self, validated_data):
        return Etiqueta.objects.create(**validated_data)
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']