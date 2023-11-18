from django import urls
from django.contrib.auth import get_user_model
import pytest

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


#Parametros POST

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