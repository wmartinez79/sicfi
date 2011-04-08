from django.db import models

class estado(models.Model):
    descripcion = models.CharField(max_length = 64)

class tipo_cliente(models.Model):
    descripcion = models.CharField(max_length = 64)
    estado = models.ForeignKey(estado)