from django import forms
from django.forms import ModelForm


from sicfi.catalogos.models import Estado, Tipo_Cliente, Pais, Departamento, Municipio, Tipo_Documento, Tipo_Direccion, Tipo_Telefono

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

class DepartamentoForm(ModelForm):
    nombre = forms.CharField(error_messages={'required':'Este campo es requerido'})
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),error_messages={'required':'Este campo es requerido'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),error_messages={'required':'Este campo es requerido'})
    class Meta:
            model = Departamento

class MunicipioForm(ModelForm):
    nombre = forms.CharField(error_messages={'required':'Este campo es requerido'})
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),error_messages={'required':'Este campo es requerido'})
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(),error_messages={'required':'Este campo es requerido'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),error_messages={'required':'Este campo es requerido'})

    class Meta:
            model = Municipio

class TipoDocumentoForm(ModelForm):
    descripcion = forms.CharField(error_messages={'required':'Este campo es requerido'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),error_messages={'required':'Este campo es requerido'})

    class Meta:
            model = Tipo_Documento

class TipoDireccionForm(ModelForm):
    descripcion = forms.CharField(error_messages={'required':'Este campo es requerido'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),error_messages={'required':'Este campo es requerido'})

    class Meta:
            model = Tipo_Direccion

class TipoTelefonoForm(ModelForm):
    descripcion = forms.CharField(error_messages={'required':'Este campo es requerido'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),error_messages={'required':'Este campo es requerido'})

    class Meta:
            model = Tipo_Telefono