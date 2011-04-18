from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from sicfi.catalogos.models import Estado, Tipo_Cliente, Pais
from sicfi.catalogos.forms import EstadoForm, TipoClienteForm, PaisForm

def listar_estados(request):
    estados = Estado.objects.all().order_by('id')
    estado_form = EstadoForm()

    return render_to_response(
        'catalogos/estado.html',
        {'estado_form' : estado_form,
         'estados': estados,
        },
        context_instance=RequestContext(request)
    )

def view_estado(request,id):
    estados = Estado.objects.all().order_by('id')
    status = get_object_or_404(Estado, pk = id)
    estado_form = EstadoForm(instance=status)

    return render_to_response(
        'catalogos/estado.html',
        {'estado_form' : estado_form,
         'estados': estados,
         'status': status
        },
        context_instance=RequestContext(request)
    )

def guardar_estado(request):
    estados = Estado.objects.all().order_by('id')

    if 'status' in request.POST:
        status_id = request.POST['status']
        status = get_object_or_404(Estado, pk = status_id)
        estado_form = EstadoForm(request.POST, instance=status)
    else:
        estado_form = EstadoForm(request.POST)
    print estado_form
    if estado_form.is_valid():
        status = estado_form.save()

        return render_to_response(
            'catalogos/estado.html',
            {'estado_form' : estado_form,
             'estados': estados,
             'status': status
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion del Estado'
        return render_to_response(
            'catalogos/estado.html',
            {'estado_form' : estado_form,
             'estados': estados,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_estado(request):
    estados = Estado.objects.all().order_by('id')
    estado_form = EstadoForm(request.POST)
    if 'status' in request.POST:
        status_id = request.POST['status']
        status = get_object_or_404(Estado, pk = status_id)
        status.delete()
        return HttpResponseRedirect('/catalogos/listar_estados/')

    else:
        mensaje_error = 'la Informacion del estado a eliminar es incorrecta'

        return render_to_response(
            'catalogos/estado.html',
            {'estado_form' : estado_form,
             'estados': estados,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def listar_tcliente(request):
    tclientes = Tipo_Cliente.objects.all().order_by('id')
    print tclientes
    tcliente_form = TipoClienteForm()

    return render_to_response(
        'catalogos/tipo_cliente.html',
        {'tcliente_form' : tcliente_form,
         'tclientes': tclientes,
        },
        context_instance=RequestContext(request)
    )

def view_tcliente(request,id):
    tclientes = Tipo_Cliente.objects.all().order_by('id')
    tclient = get_object_or_404(Tipo_Cliente, pk = id)
    tcliente_form = TipoClienteForm(instance=tclient)

    return render_to_response(
        'catalogos/tipo_cliente.html',
        {'tcliente_form' : tcliente_form,
         'tclientes': tclientes,
         'tclient': tclient
        },
        context_instance=RequestContext(request)
    )

def guardar_tcliente(request):
    tclientes = Tipo_Cliente.objects.all().order_by('id')

    if 'tclient' in request.POST:
        tclient_id = request.POST['tclient']
        tclient = get_object_or_404(Tipo_Cliente, pk = tclient_id)
        tcliente_form = TipoClienteForm(request.POST, instance=tclient)
    else:
        tcliente_form = TipoClienteForm(request.POST)
    print tcliente_form
    if tcliente_form.is_valid():
        tclient = tcliente_form.save()

        return render_to_response(
            'catalogos/tipo_cliente.html',
            {'tcliente_form' : tcliente_form,
             'tclientes': tclientes,
             'tclient': tclient
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion del Pais'
        return render_to_response(
            'catalogos/tipo_cliente.html',
            {'tcliente_form' : tcliente_form,
             'tclientes': tclientes,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_tcliente(request):
    tclientes = Tipo_Cliente.objects.all().order_by('id')
    tcliente_form = TipoClienteForm(request.POST)
    if 'tclient' in request.POST:
        tclient_id = request.POST['tclient']
        tclient = get_object_or_404(Tipo_Cliente, pk = tclient_id)
        tclient.delete()
        return HttpResponseRedirect('/catalogos/listar_tclientes/')

    else:
        mensaje_error = 'la Informacion del Pais a eliminar es incorrecta'

        return render_to_response(
            'catalogos/tipo_cliente.html',
            {'tcliente_form' : tcliente_form,
             'tclientes': tclientes,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def listar_paises(request):
    paises = Pais.objects.all().order_by('id')
    print paises
    pais_form = PaisForm()

    return render_to_response(
        'catalogos/pais.html',
        {'pais_form' : pais_form,
         'paises': paises,
        },
        context_instance=RequestContext(request)
    )

def view_pais(request,id):
    paises = Pais.objects.all().order_by('id')
    p = get_object_or_404(Pais, pk = id)
    pais_form = PaisForm(instance=p)

    return render_to_response(
        'catalogos/pais.html',
        {'pais_form' : pais_form,
         'paises': paises,
         'p': p
        },
        context_instance=RequestContext(request)
    )

def guardar_pais(request):
    paises = Pais.objects.all().order_by('id')

    if 'p' in request.POST:
        p_id = request.POST['p']
        p = get_object_or_404(Pais, pk = p_id)
        pais_form = PaisForm(request.POST, instance=p)
    else:
        pais_form = PaisForm(request.POST)
    print pais_form
    if pais_form.is_valid():
        p = pais_form.save()

        return render_to_response(
            'catalogos/pais.html',
            {'pais_form' : pais_form,
             'paises': paises,
             'p': p
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion del Pais'
        return render_to_response(
            'catalogos/pais.html',
            {'pais_form' : pais_form,
             'paises': paises,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_pais(request):
    paises = Pais.objects.all().order_by('id')
    pais_form = PaisForm(request.POST)
    if 'p' in request.POST:
        p_id = request.POST['p']
        p = get_object_or_404(Pais, pk = p_id)
        p.delete()
        return HttpResponseRedirect('/catalogos/listar_paises/')

    else:
        mensaje_error = 'Error La Informacion del pais a eliminar es incorrecta'

        return render_to_response(
            'catalogos/pais.html',
            {'pais_form' : pais_form,
             'paises': paises,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )