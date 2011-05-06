from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^/?empresa/(\d+)?$', 'sicfi.configuracion.views.view_empresa'),
    (r'^/?listar_empresas/?$', 'sicfi.configuracion.views.listar_empresas'),
    (r'^/?borrar_empresa/?$', 'sicfi.configuracion.views.delete_empresa'),
    (r'^/?guardar_empresa/?$', 'sicfi.configuracion.views.guardar_empresa'),
    
)