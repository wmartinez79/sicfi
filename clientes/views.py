# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.forms.models import inlineformset_factory
from sicfi.clientes.models import Cliente, Direccion, Telefono
from sicfi.clientes.forms import ClienteNaturalForm, ClienteJuridicoForm
from sicfi.catalogos.models import Tipo_Cliente
def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('id')

    return render_to_response(
        'clientes/clientes.html',
        {'clientes': clientes,
        },
        context_instance=RequestContext(request)
    )

def view_cliente_natural(request, cliente_id=None):
    if request.method == 'POST':
        if 'tipo' in request.POST:
            tipo = request.POST['tipo']
    else:
        if 'tipo' in request.GET:
            tipo = request.GET['tipo']

    if 'cliente' in request.POST:
        cliente_id = request.POST['cliente']

    if None == cliente_id:
        t_cliente = Tipo_Cliente.objects.get(id=1)
        cliente = Cliente(tipo_cliente=t_cliente)
    else:
        print cliente_id
        cliente = get_object_or_404(Cliente, pk = cliente_id)

    DireccionFormSet = inlineformset_factory(Cliente, Direccion, can_delete=True)
    TelefonoFormSet = inlineformset_factory(Cliente, Telefono, can_delete=True)
    mensaje_error = None
    if request.method == 'POST':
        cliente_form = ClienteNaturalForm(request.POST, instance = cliente)
        direccion_formset    = DireccionFormSet(request.POST, request.FILES, instance=cliente, prefix='direccion')
        telefono_formset  = TelefonoFormSet(request.POST, request.FILES, instance=cliente, prefix='telefono')

        if cliente_form.is_valid():
            if direccion_formset.is_valid():
                if telefono_formset.is_valid():
                    cliente_form.save()
                    direccion_formset.save()
                    telefono_formset.save()
                else:
                    mensaje_error = 'Error al guardar los telefonos'
            else:
                mensaje_error = 'Error al guardar las direcciones'
        else:
            mensaje_error = 'Error al guardar el cliente'
    else:
        print 'el method deberia ser get'
        cliente_form      = ClienteNaturalForm(instance=cliente)
        print cliente_form
        direccion_formset    = DireccionFormSet(instance=cliente, prefix='direccion')
        telefono_formset  = TelefonoFormSet(instance=cliente, prefix='telefono')

    return render_to_response('clientes/cliente_natural.html', {
        'cliente_form'        : cliente_form,
        'direccion_formset'      : direccion_formset,
        'telefono_formset'    : telefono_formset,
        'cliente'            : cliente,
        'mensaje_error'      : mensaje_error
    },
    context_instance=RequestContext(request))

