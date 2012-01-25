from django.db import models
from sicfi.smart_selects.db_fields import ChainedForeignKey
from django.utils.translation import gettext_lazy as _


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

    class Meta:
        verbose_name = _('tipo de cliente')
        verbose_name_plural = _('tipos de cliente')

class Pais(models.Model):
    nombre = models.CharField(max_length = 64)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.nombre)

    def get_absolute_url(self):
        return "/catalogos/pais/%i" % self.id

    class Meta:
        verbose_name_plural = _('paises')



class Departamento(models.Model):
    nombre = models.CharField(max_length = 64)
    pais   = models.ForeignKey(Pais)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.nombre + ' de '+ self.pais.nombre)

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

    class Meta:
        verbose_name = _('tipo de documento')
        verbose_name_plural = _('tipos de documento')

class Tipo_Direccion(models.Model):
    descripcion = models.CharField(max_length = 64)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.descripcion)

    def get_absolute_url(self):
        return "/catalogos/tdireccion/%i" % self.id

    class Meta:
        verbose_name = _('tipo de direccion')
        verbose_name_plural = _('tipos de direccion')

class Tipo_Telefono(models.Model):
    descripcion = models.CharField(max_length = 64)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % (self.descripcion)

    def get_absolute_url(self):
        return "/catalogos/ttelefono/%i" % self.id

    class Meta:
        verbose_name = _('tipo de telefono')
        verbose_name_plural = _('tipos de telefono')