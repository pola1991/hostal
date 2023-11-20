import pytest
from django.contrib.auth import get_user_model, get_backends
from app.models import *

print(get_backends())

@pytest.fixture
def cliente_user_data():
    return {
        'username':'user_name',
        'nombre_empresa':'user_company', 
        'rut_empresa':'77.123.456-6', 
        'email': 'cliente_email@email.com',
        'password1': 'SDBsda456dsa',
        'password2': 'SDBsda456dsa'
    }

@pytest.fixture
def empleado_user_data():
    return {
        'username':'user_name',
        'first_name':'name',
        'last_name':'lastname',
        'cargo':'manager', 
        'email': 'empleado_email@email.com',
        'password1': 'SDBsda456dsa',
        'password2': 'SDBsda456dsa'
    }
@pytest.fixture
def user_data():
    return {
        'username':'user_name',
        'rut_empresa':'77.123.456-6', 
        'cargo':'manager', 
        'email': 'empleado_email@email.com',
        'password': 'SDBsda456dsa'
    }

@pytest.fixture
def proveedor_data():
    return {
        'nombre': 'proveedor',
        'rubro': 'rubro proveedor',
        'contacto': '963256325',
        'otro': 'otro'
    }

@pytest.fixture
def update_proveedor_data():
    return {
        'nombre': 'Nuevo proveedor',
        'rubro': 'rubro proveedor',
        'contacto': '963256325',
        'otro': 'otro'
    }

@pytest.fixture
def habitacion_data():
    return {
        'n_habitacion': '103',
        'nombre': 'nombre',
        'precio': '25000',
        'n_camas': '3',
        'descripcion': 'hab description',
        'estado_habitacion': 'Disponible',
        'imagen':''
    }

@pytest.fixture
def update_habitacion_data():
    return {
        'n_habitacion': '103',
        'nombre': 'nuevo nombre',
        'precio': '25000',
        'n_camas': '2',
        'descripcion': 'hab description',
        'estado_habitacion': 'Disponible',
        'imagen':''
    }

@pytest.fixture
def create_proveedor_test(proveedor_data):
    proveedor_model = Proveedor
    proveedor_test = proveedor_model.objects.create(**proveedor_data)
    return proveedor_test

@pytest.fixture
def create_habitacion_test(habitacion_data):
    habitacion_model = Habitacion
    habitacion_test = habitacion_model.objects.create(**habitacion_data)
    return habitacion_test

@pytest.fixture
def create_empleado_test_user(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user


@pytest.fixture
def authenticated_user(client, user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    test_user.save()
    client.login(**user_data)
    return test_user