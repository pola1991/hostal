from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()

@given(u'Accedo a la url para registrar cliente con usuario en blanco "{url}"')
def acceso(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace para registrar cliente con usuario en blanco "{link}"')
def localizador(context,link):
    driver.implicitly_wait(5)
    time.sleep(2)
    driver.find_element(By.ID,link).click()
    
@when(u'Ingreso todos los demas datos dejando usuario en blanco')
def ingresa_solo_password(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("")
    driver.find_element(By.XPATH,"//*[@id='id_nombre_empresa']").send_keys("Empresa1")
    driver.find_element(By.XPATH,"//*[@id='id_rut_empresa']").send_keys("77.632.256-6")
    driver.find_element(By.XPATH,"//*[@id='id_email']").send_keys("empresa@email.com")
    driver.find_element(By.XPATH,"//*[@id='id_password1']").send_keys("SKANSDsdan2dsa")
    driver.find_element(By.XPATH,"//*[@id='id_password2']").send_keys("SKANSDsdan2dsa")
    time.sleep(2)
    driver.execute_script('document.querySelector("body > div > div > div > div > div.card-body > form > div.d-flex.justify-content-between > input").click()')

@then(u'Registro de cliente incorrecto con mensaje para ingresar usuario')
def no_ingreso(context):
    assert driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[1]").is_displayed()
    time.sleep(2)