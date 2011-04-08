from django.contrib.auth import REDIRECT_FIELD_NAME, views
from django.contrib.sites.models import Site, RequestSite
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from sicfi.decorators import ssl_required
from sicfi.usuario.forms import UsuarioCreacionForm

@ssl_required
def login(*args, **kwargs):
    return views.login(*args, **kwargs)

@ssl_required
def creacion_usuario(
    request,
    template_name = 'usuarios/creacion.html',
    redirect_field_name = REDIRECT_FIELD_NAME,
    usuario_creacion_form = UsuarioCreacionForm
    ):

    redirect_to = request.REQUEST.get(redirect_field_name,'')
    if 'POST' != request.method:
        usuario_form = usuario_creacion_form(data=request.GET)
    else:
        usuario_form = usuario_creacion_form(data=request.POST)

    if usuario_form.is_valid():
        print 'valido'
    else:
        print 'invalido'
        print 'usuario_form.errors'
        print repr(usuario_form.errors)

    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)
    return render_to_response(
        template_name,
        {
            'usuario_form': usuario_form,
            redirect_field_name: redirect_to,
            'site': current_site,
            'site_name': current_site.name,
        },
        context_instance=RequestContext(request))
