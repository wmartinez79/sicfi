# vim:ai:et:fenc=utf-8:ff=unix:sw=4:ts=4:

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    if request.user.is_authenticated():
        template = 'home.html'
        data = {}
    else:
        template = 'index.html'
        data = { 'form' : AuthenticationForm(request) }
    return render_to_response(
        template,
        data,
        context_instance=RequestContext(request))
