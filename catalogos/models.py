from django.db import models

class Estado(models.Model):
    descripcion = models.CharField(max_length = 64)

    def __unicode__(self):
        return u'%s' % (self.descripcion)

    def get_absolute_url(self):
        return "/catalogos/estado/%i" % self.id


class Tipo_Cliente(models.Model):
    descripcion = models.CharField(max_length = 64)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.descripcion)

    def get_absolute_url(self):
        return "/catalogos/tcliente/%i" % self.id


class Pais(models.Model):
    nombre = models.CharField(max_length = 64)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.nombre)

    def get_absolute_url(self):
        return "/catalogos/pais/%i" % self.id


class Departamento(models.Model):
    nombre = models.CharField(max_length = 64)
    pais   = models.ForeignKey(Pais)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.nombre)

    def get_absolute_url(self):
        return "/catalogos/departamento/%i" % self.id