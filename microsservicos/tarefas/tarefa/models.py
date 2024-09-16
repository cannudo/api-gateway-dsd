from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    etiqueta_id = models.IntegerField(null = True, blank = True)  # Este campo armazenará o ID da Etiqueta