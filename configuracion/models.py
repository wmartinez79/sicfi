from django.db import models
from thumbs import ImageWithThumbsField


class Empresa(models.Model):
    nombre = models.CharField(max_length = 60)
    ruc = models.CharField(max_length = 30)
    telefono = models.CharField(max_length=32, blank=True, default="")
    fax = models.CharField(max_length=32, blank=True, default="")
    email = models.TextField(blank = True)
    direccion = models.CharField(max_length = 128)
    logo = ImageWithThumbsField(upload_to='images', sizes=((125,125),(200,200)))

    def __unicode__(self):
        return u'%s' % (self.nombre)
    
    def get_absolute_url(self):
        return "/configuracion/empresa/%i" % self.id
