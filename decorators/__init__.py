import unittest
import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect


def ssl_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if settings.DEBUG or _is_secure(settings, request):
            result = view_func(request, *args, **kwargs)
        else:
            uri = request.build_absolute_uri()
            ssl = _to_ssl_uri(settings, uri)
            result = HttpResponseRedirect(ssl)
        return result
    return _wrapped_view

def _is_secure(settings, request):
    secure = False
    if request.is_secure():
        secure = True
    else:
        parts = urlparse.urlsplit(request.build_absolute_uri())
        if 'https' == parts.scheme:
            secure = True
        elif _is_ssl_port(settings, parts.port):
            secure = True
    return secure

def _is_ssl_port(settings, port):
    return (443 == port
        or (hasattr(settings, 'SSL_PORT') and settings.SSL_PORT == port))

def _to_ssl_uri(settings, uri):
    parts = urlparse.urlsplit(uri)
    host = parts.hostname
    port = parts.port
    if hasattr(settings, 'SSL_HOST'):
        host = settings.SSL_HOST
    if hasattr(settings, 'SSL_PORT'):
        port = settings.SSL_PORT
    parts = list(parts)
    parts[0] = 'https'
    parts[1] = '%s:%d' % (host, port)
    return urlparse.urlunsplit(parts)
