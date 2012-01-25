from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
   url(r'^/?login/$', 'sicfi.usuarios.views.login_view'),
)