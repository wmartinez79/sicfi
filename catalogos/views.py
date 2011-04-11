from django.template import RequestContext
from django.shortcuts import render_to_response
from sicfi.catalogos.models import Estado

def view_estado(request,id):
    estados = Estado.objects.all()

    try:
        status =  Estado.objects.get(id = id)
    except:
        print estados
        print 'sin estado'
        return render_to_response(
            'catalogos/estado.html',
            { 'estados': estados},
            context_instance=RequestContext(request)
        )
    else:
         print estados
         print 'con estado'
         return render_to_response(
            'catalogos/estado.html',
            { 'status' : status,
             'estados': estados},
            context_instance=RequestContext(request)
        )