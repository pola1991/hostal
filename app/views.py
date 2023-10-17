from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *

def home(request):
    return render(request, 'app/public/home.html')


def addProveedor(request):
    datos = {
        'form' : ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado exitosamente'

    return render(request,'app/proveedores/addProveedor.html', datos)