from django.shortcuts import render
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework import permissions, viewsets

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
