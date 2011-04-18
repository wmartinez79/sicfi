from django import forms
from django.forms import ModelForm

from sicfi.catalogos.models import Estado, Tipo_Cliente, Pais, Tipo_Documento

class EstadoForm(ModelForm):
    descripcion = forms.CharField(error_messages={'required':'Este campo es requerido'})
    class Meta:
            model = Estado

class TipoClienteForm(ModelForm):
    descripcion = forms.CharField(error_messages={'required':'Este campo es requerido'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),error_messages={'required':'Este campo es requerido'})
    class Meta:
            model = Tipo_Cliente

class PaisForm(ModelForm):
    nombre = forms.CharField(error_messages={'required':'Este campo es requerido'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),error_messages={'required':'Este campo es requerido'})
    class Meta:
            model = Pais

class TipoDocumentoForm(ModelForm):
    descripcion = forms.CharField(error_messages={'required':'Este campo es requerido'})
    class Meta:
            model = Tipo_Documento