from django.db import models

class Estado(models.Model):
    descripcion = models.CharField(max_length = 64)

    def __unicode__(self):
        return u'%s' % (self.descripcion)

class Tipo_Cliente(models.Model):
    descripcion = models.CharField(max_length = 64)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.descripcion)