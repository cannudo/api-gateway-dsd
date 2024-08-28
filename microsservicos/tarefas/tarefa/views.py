from django.shortcuts import render
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework import permissions, viewsets
from .serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
