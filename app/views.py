from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'app/public/home.html')

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
            return redirect('home') 
    return render(request, 'registration/registroCliente.html', data)

def registroEmpleado(request):
    data = {
        'form': EmpleadoForm()
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            empresa = formulario.save(commit=False)
            empresa.nombre_empresa == "Doña Clarita"
            empresa.es_empleado = True  
            empresa.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            print("Registro guardado exitosamente")
            return redirect('home') 

    return render(request, 'registration/registroEmpleado.html', data)

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

def eliminarProveedor(request, id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except:
        return redirect('readProveedor')
    if request.method == 'POST':
        proveedor.delete()
        return redirect('readProveedor')
    return render(request, 'app/proveedores/eliminarProveedor.html', {'proveedor': proveedor})

def hab(request):
    habitacion = Habitacion.objects.all()
    datos = {
        'habitacion': habitacion
    }
    return render(request,'app/Habitaciones/hab.html',datos)

def formu_create(request):
    datos = {'form': HabitacionForm()}
    if request.method == 'POST':
        formulario = HabitacionForm(request.POST)
        if formulario.is_valid():  # Agrega los paréntesis para llamar al método is_valid
            formulario.save()
            datos['mensaje'] = 'Guardado exitosamente'
            return redirect('hab')  # Redirige a la página que desees después de guardar

    return render(request, 'app/Habitaciones/form.html', datos)

def formu_update(request, id):
    try:
        habitacion = Habitacion.objects.get(id=id)
    except:
        return render(request, 'app/Habitaciones/hab.html')
    datos = {
        'form': HabitacionForm(instance=habitacion)
    }
    if request.method == 'POST':
        formulario = HabitacionForm(request.POST, instance= habitacion)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado exitosamente"
    return render(request, 'app/Habitaciones/formu_update.html', datos)

def formu_delete(request, id):
    try:
        habitacion = Habitacion.objects.get(id=id)
        habitacion.delete()
        return redirect('hab')  # Redirige a la vista 'hab' después de eliminar
    except Habitacion.DoesNotExist:
        # Manejar el caso en el que la habitación no existe
        return redirect('hab')  # Puedes redirigir a donde desees en este caso

def addComedores(request):
    data = {
        'form' : ComedorForm()
    }
    if request.method == 'POST':
        formulario = ComedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = 'Guardado exitosamente'

    return render(request,'app/comedores/addComedores.html', data)

def eliminarComedor(request, id):
    comedor = Comedor.objects.get(id=id)
    if request.method == 'POST':
        comedor.delete()
        return redirect('readComedor')

    return render(request, 'app/comedores/eliminarComedor.html', {'comedor': comedor})

def readComedor(request):
    comedor = Comedor.objects.all()
    data = {
        'comedor': comedor
    }
    return render (request, 'app/comedores/readComedor.html', data)

def huespedes(request):
    huesped = Huesped.objects.all()
    datos = {
        'huesped': huesped
    }
    return render(request,'app/Huespedes/huespedes.html',datos)

def formu_createh(request):
    datos = {'form': HuespedForm()}
    if request.method == 'POST':
        formulario = HuespedForm(request.POST)
        if formulario.is_valid():  # Agrega los paréntesis para llamar al método is_valid
            formulario.save()
            return redirect('huespedes')  # Redirige a la página que desees después de guardar

    return render(request, 'app/Huespedes/formh.html', datos)

def formu_updateh(request, id):
    try:
        huesped = Huesped.objects.get(id=id) 
    except:
        return render(request, 'app/Huespedes/huespedes.html')

    datos = {
        'form': HuespedForm(instance=huesped)
    }
    return render(request, 'app/Huespedes/form_updateh.html', datos)

def formu_deleteh(request, id):
    try:
        huesped = Huesped.objects.get(id=id)
        huesped.delete()
        return redirect('huespedes')  # Redirige a la vista 'hab' después de eliminar
    except Huesped.DoesNotExist:
        # Manejar el caso en el que la habitación no existe
        return redirect('huespedes')  # Puedes redirigir a donde desees en este caso


def delete_last_user(request):

    Usuario.objects.first().delete()

    return redirect('/accounts/logout/')