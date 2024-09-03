from rest_framework import serializers
from .models import Tarefa
import requests

class TarefaSerializer(serializers.ModelSerializer):
    etiqueta_id = serializers.IntegerField(required = False, allow_null = True)

    class Meta:
        model = Tarefa
        fields = ['id', 'nome', 'descricao', 'etiqueta_id']

        extra_kwargs = {
            'etiqueta_id': {'required': False, 'allow_null': True},
        }

    def validate_etiqueta_id(self, value):
        # Verifica se a etiqueta existe
        if value:
            print("Value = ", value)
            url = f'http://localhost:8000/etiquetas/{value}/'
            response = requests.get(url)
            if response.status_code != 200:
                raise serializers.ValidationError("Etiqueta não encontrada.")
            return value
        else:
            pass

    def create(self, validated_data):
        try:
            etiqueta_id = validated_data.pop('etiqueta_id')
        except KeyError:
            etiqueta_id = None
        return Tarefa.objects.create(etiqueta_id=etiqueta_id, **validated_data)