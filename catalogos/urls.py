from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^/?estado/(\d+)?$', 'sicfi.catalogos.views.view_estado'),
    (r'^/?tipo_cliente/?$', 'sicfi.catalogos.views.view_tipo_cliente'),
)