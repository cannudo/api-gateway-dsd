from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    etiqueta = models.CharField(max_length=50)