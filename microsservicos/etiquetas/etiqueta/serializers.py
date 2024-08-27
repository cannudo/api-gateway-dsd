from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Etiqueta

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = "__all__"   
        