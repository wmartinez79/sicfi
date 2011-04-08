from django import forms
from django.contrib import auth

from sicfi.usuarios.models import Usuario

class UsuarioCreacionForm(auth.forms.UserCreationForm):
    email1 = forms.EmailField('Email')
    email1 = forms.EmailField('Confirmación del Email')
    tel = forms.CharField(max_length = 32)

    class Meta:
        model = Usuario
        fields = ('tel')