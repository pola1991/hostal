from django import urls
from django.contrib.auth import get_user_model
import pytest


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


@pytest.mark.parametrize('param', [
    ('formu_update'),
])
@pytest.mark.django_db
def test_render_views_with_params(client, param):
    temp_url = urls.reverse(param, kwargs={"id":"2"})
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.parametrize('param', [
    ('eliminarProveedor'),
    ('formu_delete'),
])
@pytest.mark.django_db
def test_render_views_delete(client, param):
    temp_url = urls.reverse(param, kwargs={"id":"1"})
    resp = client.get(temp_url)
    assert resp.status_code == 302