from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class clienteForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [ "username" ,"nombre_empresa", "rut_empresa", "email", "password1", "password2"]



class ProveedorForm(forms.ModelForm):
    class Meta: 
        model = Proveedor
        fields = ['nombre', 'rubro', 'contacto', 'otro']


class usuarioForm(forms.ModelForm):
        class Meta:
            models = Usuario
            if (Usuario.es_cliente) == True:
                fields = ['nombre_empresa', 'rut_empresa','email','imagen']
            if (Usuario.es_empleado) == True:
                 fields = ['first_name', 'last_name', 'cargo', 'email']