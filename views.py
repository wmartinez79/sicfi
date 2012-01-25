from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    print 'request.user -->'
    print request.user
    print request
    if request.user.is_authenticated():
        print 'autenticado'
        template = 'home.html'
        data = {}
    else:
        print 'no autenticado'
        template = 'registration/login.html'
        data = { 'form' : AuthenticationForm(request) }
    return render_to_response(
        template,
        data,
        context_instance=RequestContext(request))
