from sicfi.catalogos.models import Estado, Tipo_Cliente, Departamento, Municipio, Pais, Tipo_Documento, Tipo_Direccion, Tipo_Telefono
from django.contrib import admin

admin.site.register(Estado)
admin.site.register(Tipo_Cliente)
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Tipo_Documento)
admin.site.register(Tipo_Direccion)
admin.site.register(Tipo_Telefono)
