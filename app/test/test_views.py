from django import urls
from django.contrib.auth import get_user_model
import pytest
from app.models import *

#Parametros GET
@pytest.mark.parametrize('param', [
    ('home'),
    ('login'),
    ('registroCliente'),
    ('registroEmpleado'),
    ('perfilCliente'),
    ('addProveedor'),
    ('readProveedor'),
    ('hab'),
    ('formu_create'),
])
@pytest.mark.django_db
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200

#registro cliente
@pytest.mark.django_db
def test_cliente_signup(client, cliente_user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('registroCliente')
    resp = client.post(signup_url,cliente_user_data)
    assert user_model.objects.count() == 1
    assert resp.status_code == 302

#registro de empleado
@pytest.mark.django_db
def test_empleado_signup(client, empleado_user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('registroEmpleado')
    resp = client.post(signup_url,empleado_user_data)
    assert user_model.objects.count() == 1
    assert resp.status_code == 302

#Login de usuario
@pytest.mark.django_db
def test_user_login(client, create_empleado_test_user,user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('login')
    resp = client.post(login_url, data=user_data)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('home')

#Logout
@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = urls.reverse('logout')
    resp = client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('home')

#Crear proveedor
@pytest.mark.django_db
def test_crear_proveedor(client, proveedor_data):
    proveedor_model = Proveedor
    assert proveedor_model.objects.count() == 0
    add_proveedor_url = urls.reverse('addProveedor')
    resp = client.post(add_proveedor_url,proveedor_data)
    assert proveedor_model.objects.count() == 1
    assert resp.status_code == 200

#Eliminar proveedor
@pytest.mark.django_db
def test_delete_proveedor(client, create_proveedor_test):
    proveedor_model = Proveedor
    assert proveedor_model.objects.count() == 1
    delete_proveedor_url = urls.reverse('eliminarProveedor', kwargs= {'id': proveedor_model.objects.first().pk })
    resp = client.delete(delete_proveedor_url)
    assert resp.status_code == 200

#Crear habitacion
@pytest.mark.django_db
def test_crear_habitacion(client, habitacion_data):
    habitacion_model = Habitacion
    assert habitacion_model.objects.count() == 0
    add_habitacion_url = urls.reverse('formu_create')
    resp = client.post(add_habitacion_url,habitacion_data)
    assert habitacion_model.objects.count() == 1
    assert resp.status_code == 302

#Modificar habitacion
@pytest.mark.django_db
def test_update_habitacion(client, create_habitacion_test, update_habitacion_data):
    habitacion_model = Habitacion
    assert habitacion_model.objects.count() == 1
    uptade_habitacion_url = urls.reverse('formu_update', kwargs= {'id': habitacion_model.objects.first().pk })
    resp = client.update(uptade_habitacion_url, update_habitacion_data)
    assert resp.status_code == 302

#Eliminar habitacion
@pytest.mark.django_db
def test_delete_habitacion(client, create_habitacion_test):
    habitacion_model = Habitacion
    assert habitacion_model.objects.count() == 1
    delete_habitacion_url = urls.reverse('formu_update', kwargs= {'id': habitacion_model.objects.first().pk })
    resp = client.delete(delete_habitacion_url)
    assert resp.status_code == 200