from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()
@given(u'Accedo a la url para darle clik a boton contacto "{url}"')
def step_acceso_a_la_url5(context,url):
    driver.get("http://127.0.0.1:8000/accounts/logout/")
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace de contacto "{link}"')
def localiza_enlace_logi5(context,link):
    time.sleep(2)
    driver.find_element(By.ID,link).click()
    
@then(u'Me redirecciona al apartado de contacto')
def ingresa_a_la_cuenta(context):
    assert driver.find_element(By.XPATH,"//*[@id='contacto']/h2").is_displayed()
    driver.get("http://127.0.0.1:8000/accounts/logout/")