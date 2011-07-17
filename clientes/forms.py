from django import forms
from django.forms import ModelForm
from sicfi.clientes.models import Cliente, Direccion, Telefono
from sicfi.catalogos.models import Tipo_Cliente, Tipo_Documento, Tipo_Direccion, Pais, Departamento, Municipio, Tipo_Telefono

class ClienteNaturalForm(ModelForm):
    primer_nombre = forms.CharField(error_messages={'required':'Este campo es requerido'})
    segundo_nombre = forms.CharField()
    primer_apellido = forms.CharField(error_messages={'required':'Este campo es requerido'})
    segundo_apellido = forms.CharField()
    tipo_documento = forms.ModelChoiceField(queryset=Tipo_Documento.objects.all(),error_messages={'required':'Este campo es requerido'})
    numero_documento = forms.CharField(error_messages={'required':'Este campo es requerido'})
    exento = forms.BooleanField(required=False)
    email = forms.EmailField(error_messages={'required':'Este campo es requerido'})


class ClienteJuridicoForm(ModelForm):
    razon_social = forms.CharField(error_messages={'required':'Este campo es requerido'})
    nombre_comercial = forms.CharField(error_messages={'required':'Este campo es requerido'})
    tipo_documento = forms.ModelChoiceField(queryset=Tipo_Documento.objects.all(),error_messages={'required':'Este campo es requerido'})
    numero_documento = forms.CharField(error_messages={'required':'Este campo es requerido'})
    exento = forms.BooleanField(error_messages={'required':'Este campo es requerido'})
    email = forms.EmailField(error_messages={'required':'Este campo es requerido'})

    class Meta:
            model = Cliente

class Direccion(ModelForm):
    direccion = forms.CharField(error_messages={'required':'Este campo es requerido'})
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(),error_messages={'required':'Este campo es requerido'})
    tipo_direccion = forms.ModelChoiceField(queryset=Tipo_Direccion.objects.all(),error_messages={'required':'Este campo es requerido'})
    class Meta:
            model = Direccion

class Telefono(ModelForm):
    telefono = forms.CharField(error_messages={'required':'Este campo es requerido'})
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(),error_messages={'required':'Este campo es requerido'})
    tipo_telefono = forms.ModelChoiceField(queryset=Tipo_Direccion.objects.all(),error_messages={'required':'Este campo es requerido'})