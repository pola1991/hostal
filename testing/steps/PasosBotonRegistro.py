from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()
@given(u'Accedo a la url para darle clik a boton registrar "{url}"')
def step_acceso_a_la_url5(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'hago click en enlace de registrarse "{link}"')
def localiza_enlace_logi5(context,link):
    time.sleep(2)
    driver.find_element(By.ID,link).click()
    
@then(u'Puedo ingresar a la pagina de registro')
def ingresa_a_la_cuenta(context):
    time.sleep(2)
    assert driver.current_url == "http://127.0.0.1:8000/registroCliente/"