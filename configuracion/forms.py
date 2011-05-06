from django import forms
from django.forms import ModelForm


from sicfi.configuracion.models import Empresa

class EmpresaForm(ModelForm):
    nombre = forms.CharField(error_messages={'required':'Este campo es requerido'})
    ruc = forms.CharField()
    telefono = forms.CharField(error_messages={'required':'Este campo es requerido'})
    fax = forms.CharField()
    email = forms.CharField()
    direccion = forms.CharField()
    class Meta:
            model = Empresa