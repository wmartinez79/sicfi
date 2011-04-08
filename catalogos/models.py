from django.db import models
import sicfi.usuarios.models as users

class estados(models.Model):
    descripcion = models.CharField(max_length = 64)