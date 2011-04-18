from django.db import models
from sicfi.smart_selects.db_fields import ChainedForeignKey


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
        return u'%s' % (self.nombre + ' de '+ self.pais)

    def get_absolute_url(self):
        return "/catalogos/departamento/%i" % self.id

class Municipio(models.Model):
    nombre = models.CharField(max_length = 64)
    pais   = models.ForeignKey(Pais)
    departamento = ChainedForeignKey(
        Departamento,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True
    )
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.nombre)

    def get_absolute_url(self):
        return "/catalogos/municipio/%i" % self.id

class Tipo_Documento(models.Model):
    descripcion = models.CharField(max_length = 64)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.descripcion)

    def get_absolute_url(self):
        return "/catalogos/tdocumento/%i" % self.id

