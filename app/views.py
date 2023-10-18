from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'app/public/home.html')


def loginEmpresa(request):
    data = {
        'form' : CustomAuthenticationForm
    }
    if request.method == 'POST':
        form = CustomAuthenticationForm
        form.save

    return  render(request, 'registration/loginEmpresa.html', data)


def addProveedor(request):
    data = {
        'form' : ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = 'Guardado exitosamente'

    return render(request,'app/proveedores/addProveedor.html', data)




def registroCliente(request):

    data = {
        'form': clienteForm()
    }

    if request.method == 'POST':
        formulario = clienteForm(data=request.POST)
        if formulario.is_valid():
            empresa = formulario.save(commit=False)
            empresa.es_cliente = True  # Establece el campo es_cliente en la instancia del modelo
            empresa.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            print("Registro guardado exitosamente")
            return redirect('home')  # Reemplaza 'home' con el nombre de tu vista de página de inicio

    return render(request, 'registration/registroCliente.html', data)


def readProveedor(request):
    proveedor = Proveedor.objects.all()
    data = {
        'proveedor': proveedor
    }
    return render (request, 'app/proveedores/readProveedor.html', data)


def readCliente(request):
    clientes = Usuario.objects.filter(cliente = Usuario.es_cliente == True)

    data = {
        'cliente': clientes
    }
    return render (request, 'app/proveedores/readProveedor.html', data)


def perfilCliente(request):
    

    return render(request, 'app/clientes/perfilCliente.html')