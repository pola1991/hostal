import pytest
from django.contrib.auth import get_user_model

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