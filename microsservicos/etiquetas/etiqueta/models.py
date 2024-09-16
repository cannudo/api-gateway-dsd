from django.db import models

class Etiqueta(models.Model):
    titulo = models.CharField(max_length = 25)
    descricao = models.CharField(max_length = 75)