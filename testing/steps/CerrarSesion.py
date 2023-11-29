from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()
@given(u'Ingreso a la url para hacer inicio de sesion "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get("http://127.0.0.1:8000/accounts/logout/")
    driver.get(url)
    driver.maximize_window()

@when(u'Ingreso las credenciales e ingreso a la cuenta')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME,'password').send_keys('paula')
    time.sleep(2)
    driver.find_element(By.ID,"loginBtn").click()

@when(u'Apreto el link para cerrar sesion')
def apreto_link_para_cerrar_sesion(context):
    time.sleep(2)
    driver.find_element(By.ID,"linkCerrarSesion").click()

@then(u'Regreso al home page con la sesion cerrada')
def regreso_con_sesion_cerrada(context):
    time.sleep(2)
    assert driver.find_element(By.ID,"linkIniciarSesion").is_displayed()