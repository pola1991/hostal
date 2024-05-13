from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()


@given(u'Accedo a la url para hacer login con usuario incorrecto "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'hago click en enlace para hacer inicio de sesion con usuario incorrecto "{link}"')
def localiza_enlace_login(context,link):
    driver.implicitly_wait(5)
    time.sleep(1)
    driver.find_element(By.ID,link).click()
    

@when(u'Ingresa las credenciales de acceso con usuario incorrecto')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("pola")
    driver.find_element(By.NAME,'password').send_keys('paula')
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@then(u'Recibo mensaje inicio de sesion incorrecto (usuario)')
def ingresa_a_la_cuenta(context):
    assert driver.current_url == "http://127.0.0.1:8000/accounts/login/"
    time.sleep(2)