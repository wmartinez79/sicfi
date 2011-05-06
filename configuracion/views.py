from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from sicfi.configuracion.models import Empresa
from sicfi.configuracion.forms import EmpresaForm



def listar_empresas(request):
    empresas = Empresa.objects.all().order_by('id')
    print empresas
    empresa_form = EmpresaForm()

    return render_to_response(
        'configuracion/empresa.html',
        {'empresa_form' : empresa_form,
         'empresas': empresas,
        },
        context_instance=RequestContext(request)
    )

def view_empresa(request,id):
    empresas = Empresa.objects.all().order_by('id')
    empresa = get_object_or_404(Empresa, pk = id)
    empresa_form = EmpresaForm(instance=empresa)

    return render_to_response(
        'configuracion/empresa.html',
        {'empresa_form' : empresa_form,
         'empresas': empresas,
         'empresa': empresa
        },
        context_instance=RequestContext(request)
    )

def guardar_empresa(request):
    empresas = Empresa.objects.all().order_by('id')

    if 'empr' in request.POST:
        empresa_id = request.POST['empr']
        empr = get_object_or_404(Empresa, pk = empresa_id)
        empresa_form = TipoTelefonoForm(request.POST, instance=empr)
    else:
        empresa_form = TipoTelefonoForm(request.POST)
    print empresa_form
    if empresa_form.is_valid():
        empr = empresa_form.save()

        return render_to_response(
            'configuracion/empresa.html',
            {'empresa_form' : empresa_form,
             'empresas': empresas,
             'empr': empr
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion de la Empresa'
        return render_to_response(
            'configuracion/empresa.html',
            {'empresa_form' : empresa_form,
             'empresas': empresas,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_empresa(request):
    empresas = Empresa.objects.all().order_by('id')
    empresa_form = EmpresaForm(request.POST)
    if 'empr' in request.POST:
        empresa_id = request.POST['empr']
        empr = get_object_or_404(Empresa, pk = empresa_id)
        empr.delete()
        return HttpResponseRedirect('/configuracion/listar_empresa/')

    else:
        mensaje_error = 'la Informacion de la Empresa a eliminar es incorrecta'

        return render_to_response(
            'configuracion/empresa.html',
            {'empresa_form' : empresa_form,
             'empresas': empresas,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )
