from django.db import models
from sicfi.smart_selects.db_fields import ChainedForeignKey
from sicfi.catalogos.models import Tipo_Cliente, Tipo_Documento, Tipo_Direccion, Pais, Departamento, Municipio, Tipo_Telefono

class Cliente(models.Model):
    primer_nombre = models.CharField(max_length = 64)
    segundo_nombre = models.CharField(max_length = 64)
    primer_apellido = models.CharField(max_length = 64)
    segundo_apellido = models.CharField(max_length = 64)
    razon_social = models.CharField(max_length = 120)
    nombre_comercial = models.CharField(max_length = 120)
    representante_legal= models.CharField(max_length = 80)
    tipo_cliente = models.ForeignKey(Tipo_Cliente)
    tipo_documento = models.ForeignKey(Tipo_Documento)
    numero_documento = models.CharField(max_length = 30)
    exento_ir = models.BooleanField()
    email = models.EmailField()

    def get_nombre(self):
        if self.tipo_cliente == Tipo_Cliente.objects.get(descripcion='Natural'):
            return u'%s' % (self.primer_nombre + self.primer_apellido + self.segundo_apellido)
        else:
            return u'%s' % (self.nombre_comercial)

    def __unicode__(self):
        return self.get_nombre()

    def get_absolute_url(self):
        if self.tipo_cliente.id == 1:
            return "/clientes/cliente_natural/%i" % self.id
        else:
            return "/clientes/cliente_juridico/%i" % self.id



class Direccion(models.Model):
    direccion = models.CharField(max_length = 120)
    cliente = models.ForeignKey(Cliente)
    tipo_direccion = models.ForeignKey(Tipo_Direccion)
    pais = models.ForeignKey(Pais)
    departamento = ChainedForeignKey(
        Departamento,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True
    )
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )

    def __unicode__(self):
        return u'%s' % (self.direccion)

    def get_absolute_url(self):
        return "/clientes/direccion/%i" % self.id

class Telefono(models.Model):
    telefono = models.CharField(max_length = 15)
    cliente = models.ForeignKey(Cliente)
    tipo_telefono = models.ForeignKey(Tipo_Telefono)

    def __unicode__(self):
        return u'%s' % (self.telefono)

    def get_absolute_url(self):
        return "/clientes/telefono/%i" % self.id
