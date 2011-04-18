from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^/?estado/(\d+)?$', 'sicfi.catalogos.views.view_estado'),
    (r'^/?listar_estados/?$', 'sicfi.catalogos.views.listar_estados'),
    (r'^/?borrar_estado/?$', 'sicfi.catalogos.views.delete_estado'),
    (r'^/?guardar_estado/?$', 'sicfi.catalogos.views.guardar_estado'),
    (r'^/?tcliente/(\d+)?$', 'sicfi.catalogos.views.view_tcliente'),
    (r'^/?listar_tclientes/?$', 'sicfi.catalogos.views.listar_tclientes'),
    (r'^/?borrar_tcliente/?$', 'sicfi.catalogos.views.delete_tcliente'),
    (r'^/?guardar_tcliente/?$', 'sicfi.catalogos.views.guardar_tcliente'),

)