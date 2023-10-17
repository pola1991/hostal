from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class ProveedorForm(forms.ModelForm):
    class Meta: 
        model = Proveedor
        fields = ['nombre', 'rubro', 'contacto', 'otro']
