from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()
@given(u'Accedo a la url para darle clik a boton inicio de sesion "{url}"')
def step_acceso_a_la_url5(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace de inicio de sesion "{link}"')
def localiza_enlace_logi5(context,link):
    time.sleep(2)
    driver.find_element(By.ID,link).click()
    
@then(u'Puedo ingresar a la pagina de inicio de sesion')
def ingresa_a_la_cuenta(context):
    
    assert driver.current_url == "http://127.0.0.1:8000/accounts/login/"