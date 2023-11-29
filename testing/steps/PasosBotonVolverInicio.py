from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()
@given(u'Accedo a la url para darle clik a boton inicio de sesion y luego volver a inicio "{url}"')
def step_acceso_a_la_url5(context,url):
    driver.get("http://127.0.0.1:8000/accounts/logout/")
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace de inicio de sesion y luego volver a inicio "{link}"')
def localiza_enlace_logi5(context,link):
    time.sleep(2)
    driver.find_element(By.ID,link).click()
    
@when(u'Logro ingresar a la pagina de inicio de sesion')
def ingresa_a_la_cuenta(context):
    assert driver.current_url == "http://127.0.0.1:8000/accounts/login/"
    
@when(u'Hago clik en boton volver inicio "{link}"')
def localiza_enlace(context,link):
    time.sleep(2)
    driver.find_element(By.ID,link).click()


@then(u'Me redireccionara a home')
def regreso_a_inicio(context):
    assert driver.current_url == "http://127.0.0.1:8000/"
    driver.get("http://127.0.0.1:8000/accounts/logout/")