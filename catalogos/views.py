from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from sicfi.catalogos.models import Estado, Tipo_Cliente, Pais, Departamento, Municipio, Tipo_Documento, Tipo_Direccion
from sicfi.catalogos.forms import EstadoForm, TipoClienteForm, PaisForm, DepartamentoForm, MunicipioForm, TipoDocumentoForm, TipoDireccionForm

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
        return HttpResponseRedirect('/catalogos/listar_tcliente/')

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
        mensaje_error = 'Error - La Informacion del pais a eliminar es incorrecta'

        return render_to_response(
            'catalogos/pais.html',
            {'pais_form' : pais_form,
             'paises': paises,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def listar_departamentos(request):
    departamentos = Departamento.objects.all().order_by('id')
    departamento_form = DepartamentoForm()

    return render_to_response(
        'catalogos/departamento.html',
        {'departamento_form' : departamento_form,
         'departamentos': departamentos,
        },
        context_instance=RequestContext(request)
    )


def view_departamento(request,id):
    departamentos = Departamento.objects.all().order_by('id')
    depa = get_object_or_404(Departamento, pk = id)
    departamento_form = DepartamentoForm(instance=depa)

    return render_to_response(
        'catalogos/departamento.html',
        {'departamento_form' : departamento_form,
         'departamentos': departamentos,
         'depa': depa
        },
        context_instance=RequestContext(request)
    )


def guardar_departamento(request):
    departamentos = Departamento.objects.all().order_by('id')

    if 'depa' in request.POST:
        depa_id = request.POST['depa']
        depa = get_object_or_404(Departamento, pk = depa_id)
        departamento_form = DepartamentoForm(request.POST, instance=depa)
    else:
        departamento_form = DepartamentoForm(request.POST)

    if departamento_form.is_valid():
        depa = departamento_form.save()

        return render_to_response(
            'catalogos/departamento.html',
            {'departamento_form' : departamento_form,
             'departamentos': departamentos,
             'depa': depa
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion del Departamento'
        return render_to_response(
            'catalogos/departamento.html',
            {'departamento_form' : departamento_form,
             'departamentos': departamentos,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_departamento(request):
    departamentos = Departamento.objects.all().order_by('id')
    departamento_form = DepartamentoForm(request.POST)
    if 'depa' in request.POST:
        depa_id = request.POST['depa']
        depa = get_object_or_404(Departamento, pk = depa_id)
        depa.delete()
        return HttpResponseRedirect('/catalogos/listar_departamentos/')

    else:
        mensaje_error = 'Error - La Informacion del Departamento a eliminar es incorrecta'

        return render_to_response(
            'catalogos/departamento.html',
            {'Departamento_form' : departamento_form,
             'departamentos': departamentos,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def listar_municipios(request):
    municipios = Municipio.objects.all().order_by('id')
    municipio_form = MunicipioForm()

    return render_to_response(
        'catalogos/municipio.html',
        {'municipio_form' : municipio_form,
         'municipios': municipios,
        },
        context_instance=RequestContext(request)
    )

def view_municipio(request,id):
    municipios = Municipio.objects.all().order_by('id')
    muni = get_object_or_404(Municipio, pk = id)
    municipio_form = municipioForm(instance=muni)

    return render_to_response(
        'catalogos/municipio.html',
        {'municipio_form' : municipio_form,
         'municipios': municipios,
         'muni': muni
        },
        context_instance=RequestContext(request)
    )

def guardar_municipio(request):
    municipios = Municipio.objects.all().order_by('id')

    if 'muni' in request.POST:
        muni_id = request.POST['muni']
        muni = get_object_or_404(Municipio, pk = muni_id)
        municipio_form = MunicipioForm(request.POST, instance=muni)
    else:
        municipio_form = MunicipioForm(request.POST)

    if municipio_form.is_valid():
        muni = municipio_form.save()

        return render_to_response(
            'catalogos/municipio.html',
            {'municipio_form' : municipio_form,
             'municipios': municipios,
             'muni': muni
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion del municipio'
        return render_to_response(
            'catalogos/municipio.html',
            {'municipio_form' : municipio_form,
             'municipios': municipios,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_municipio(request):
    municipios = Municipio.objects.all().order_by('id')
    municipio_form = MunicipioForm(request.POST)
    if 'muni' in request.POST:
        muni_id = request.POST['muni']
        muni = get_object_or_404(Municipio, pk = muni_id)
        muni.delete()
        return HttpResponseRedirect('/catalogos/listar_municipios/')

    else:
        mensaje_error = 'Error - La Informacion del municipio a eliminar es incorrecta'

        return render_to_response(
            'catalogos/municipio.html',
            {'municipio_form' : municipio_form,
             'municipioes': municipios,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def listar_tdocumento(request):
    tdocumentos = Tipo_Documento.objects.all().order_by('id')
    print tdocumentos
    tdocumento_form = TipoDocumentoForm()

    return render_to_response(
        'catalogos/tipo_documento.html',
        {'tdocumento_form' : tdocumento_form,
         'tdocumentos': tdocumentos,
        },
        context_instance=RequestContext(request)
    )

def view_tdocumento(request,id):
    tdocumentos = Tipo_Documento.objects.all().order_by('id')
    tdocumento = get_object_or_404(Tipo_Documento, pk = id)
    tdocumento_form = TipoDocumentoForm(instance=tdocumento)

    return render_to_response(
        'catalogos/tipo_documento.html',
        {'tdocumento_form' : tdocumento_form,
         'tdocumentos': tdocumentos,
         'tdocumento': tdocumento
        },
        context_instance=RequestContext(request)
    )

def guardar_tdocumento(request):
    tdocumentos = Tipo_Documento.objects.all().order_by('id')

    if 'tdocumento' in request.POST:
        tdocumento_id = request.POST['tdocumento']
        tdocumento = get_object_or_404(Tipo_Documento, pk = tdocumento_id)
        tdocumento_form = TipoDocumentoForm(request.POST, instance=tdocumento)
    else:
        tdocumento_form = TipoDocumentoForm(request.POST)

    if tdocumento_form.is_valid():
        tdocumento = tdocumento_form.save()

        return render_to_response(
            'catalogos/tipo_documento.html',
            {'tdocumento_form' : tdocumento_form,
             'tdocumentos': tdocumentos,
             'tdocumento': tdocumento
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion del Tipo de Documento'
        return render_to_response(
            'catalogos/tipo_documento.html',
            {'tdocumento_form' : tdocumento_form,
             'tdocumentos': tdocumentos,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_tdocumento(request):
    tdocumentos = Tipo_Documento.objects.all().order_by('id')
    tdocumento_form = TipoDocumentoForm(request.POST)
    if 'tdocumento' in request.POST:
        tdocumento_id = request.POST['tdocumento']
        tdocumento = get_object_or_404(Tipo_Documento, pk = tdocumento_id)
        tdocumento.delete()
        return HttpResponseRedirect('/catalogos/listar_tdocumento/')

    else:
        mensaje_error = 'la Informacion del tipo de documento a eliminar es incorrecta'

        return render_to_response(
            'catalogos/tipo_documento.html',
            {'documento_form' : tdocumento_form,
             'tdocumentos': tdocumentos,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def listar_tdireccion(request):
    tdirecciones = Tipo_Direccion.objects.all().order_by('id')
    print tdirecciones
    tdireccion_form = TipoDireccionForm()

    return render_to_response(
        'catalogos/tipo_direccion.html',
        {'tdireccion_form' : tdireccion_form,
         'tdirecciones': tdirecciones,
        },
        context_instance=RequestContext(request)
    )

def view_tdireccion(request,id):
    tdirecciones = Tipo_Direccion.objects.all().order_by('id')
    tdireccion = get_object_or_404(Tipo_Direccion, pk = id)
    tdireccion_form = TipoDireccionForm(instance=tdireccion)

    return render_to_response(
        'catalogos/tipo_direccion.html',
        {'tdireccion_form' : tdireccion_form,
         'tdirecciones': tdirecciones,
         'tdireccion': tdireccion
        },
        context_instance=RequestContext(request)
    )

def guardar_tdireccion(request):
    tdirecciones = Tipo_Direccion.objects.all().order_by('id')

    if 'tdireccion' in request.POST:
        tdireccion_id = request.POST['tdireccion']
        tdireccion = get_object_or_404(Tipo_Direccion, pk = tdireccion_id)
        tdireccion_form = TipoDireccionForm(request.POST, instance=tdireccion)
    else:
        tdireccion_form = TipoDireccionForm(request.POST)
    print tdireccion_form
    if tdireccion_form.is_valid():
        tdireccion = tdireccion_form.save()

        return render_to_response(
            'catalogos/tipo_direccion.html',
            {'tdireccion_form' : tdireccion_form,
             'tdirecciones': tdirecciones,
             'tdireccion': tdireccion
            },
            context_instance=RequestContext(request)
        )
    else:
        mensaje_error = 'Error al guardar la informacion del Tipo de Direccion'
        return render_to_response(
            'catalogos/tipo_direccion.html',
            {'tdireccion_form' : tdireccion_form,
             'tdirecciones': tdirecciones,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )

def delete_tdireccion(request):
    tdirecciones = Tipo_Direccion.objects.all().order_by('id')
    tdireccion_form = TipoDireccionForm(request.POST)
    if 'tdireccion' in request.POST:
        tdireccion_id = request.POST['tdireccion']
        tdireccion = get_object_or_404(Tipo_Direccion, pk = tdireccion_id)
        tdireccion.delete()
        return HttpResponseRedirect('/catalogos/listar_tdireccion/')

    else:
        mensaje_error = 'la Informacion del Tipo de Direccion a eliminar es incorrecta'

        return render_to_response(
            'catalogos/tipo_direccion.html',
            {'tdireccion_form' : tdireccion_form,
             'tdirecciones': tdirecciones,
             'mensaje_error' : mensaje_error
            },
            context_instance=RequestContext(request)
        )
