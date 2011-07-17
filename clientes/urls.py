from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^/?cliente_natural/(\d+)?$', 'sicfi.clientes.views.view_cliente_natural'),
    (r'^/?listar_clientes/?$', 'sicfi.clientes.views.listar_clientes'),
)