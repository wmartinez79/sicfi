from django.contrib.auth import views
from sicfi.decorators import ssl_required

@ssl_required
def login_view(*args, **kwargs):
    return views.login(*args, **kwargs)