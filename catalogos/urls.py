from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^/?estado/(\d+)?$', 'sicfi.catalogos.views.view_estado'),
    (r'^/?listar_estados/?$', 'sicfi.catalogos.views.listar_estados'),
    (r'^/?borrar_estado/?$', 'sicfi.catalogos.views.delete_estado'),
    (r'^/?guardar_estado/?$', 'sicfi.catalogos.views.guardar_estado'),
    (r'^/?tcliente/(\d+)?$', 'sicfi.catalogos.views.view_tcliente'),
    (r'^/?listar_tcliente/?$', 'sicfi.catalogos.views.listar_tcliente'),
    (r'^/?borrar_tcliente/?$', 'sicfi.catalogos.views.delete_tcliente'),
    (r'^/?guardar_tcliente/?$', 'sicfi.catalogos.views.guardar_tcliente'),
    (r'^/?pais/(\d+)?$', 'sicfi.catalogos.views.view_pais'),
    (r'^/?listar_paises/?$', 'sicfi.catalogos.views.listar_paises'),
    (r'^/?borrar_pais/?$', 'sicfi.catalogos.views.delete_pais'),
    (r'^/?guardar_pais/?$', 'sicfi.catalogos.views.guardar_pais'),
    (r'^/?departamento/(\d+)?$', 'sicfi.catalogos.views.view_departamento'),
    (r'^/?listar_departamentos/?$', 'sicfi.catalogos.views.listar_departamentos'),
    (r'^/?borrar_departamento/?$', 'sicfi.catalogos.views.delete_departamento'),
    (r'^/?guardar_departamento/?$', 'sicfi.catalogos.views.guardar_departamento'),
    (r'^/?municipio/(\d+)?$', 'sicfi.catalogos.views.view_municipio'),
    (r'^/?listar_municipios/?$', 'sicfi.catalogos.views.listar_municipios'),
    (r'^/?borrar_municipio/?$', 'sicfi.catalogos.views.delete_municipio'),
    (r'^/?guardar_municipio/?$', 'sicfi.catalogos.views.guardar_municipio'),

)