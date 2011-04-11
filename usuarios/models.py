from django.db import models
from django.contrib.auth.models import User


class Permiso(models.Model):
    """
    Los estados deben estar representados en una clase aparte, ojo, se
    podria crear en los modelos de los catalogos
    """
    PERMISO_ESTADOS = (
        ('A','Activo'),
        ('I','Inactivo')
    )
    nombre = models.CharField(max_length= 64)
    estado = models.CharField(max_length = 2, choices=PERMISO_ESTADOS)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modi = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return u'%s' % (self.nombre)

class Rol(models.Model):
    ROL_ESTADOS = (
        ('A','Activo'),
        ('I','Inactivo')
    )
    nombre = models.CharField(max_length= 64)
    estado = models.CharField(max_length = 2, choices=ROL_ESTADOS)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modi = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return u'%s' % (self.nombre)

class Rol_Permiso(models.Model):
    permiso = models.ForeignKey(Permiso)
    rol = models.ForeignKey(Rol)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modi = models.DateTimeField(auto_now = True)

class Usuario(models.Model):
    usuario = models.ForeignKey(
        User, to_field='username',unique=True, editable=False
    )
    nombres = models.CharField(max_length = 60)
    primer_apellido = models.CharField(max_length = 32)
    segundo_apellido = models.CharField(max_length = 32, blank = True)
    numero_documento = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 128)
    telefono = models.CharField(max_length=32, blank=True, default="")
    email = models.TextField(blank = True)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modi = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return u'%s' % (self.usuario)

class Usuario_Rol(models.Model):
    usuario = models.ForeignKey(Usuario, to_field='usuario')
    permiso = models.ForeignKey(Permiso)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modi = models.DateTimeField(auto_now = True)