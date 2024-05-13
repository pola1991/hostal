from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()


@given(u'Accedo a la url para hacer login con usuario y password en blanco "{url}"')
def acceso4(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace para hacer inicio de sesion con usuario y password en blanco "{link}"')
def localizador4(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.ID,link).click()
    

@when(u'Dejo en blanco usuario y password')
def ingreso_en_blanco(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("")
    driver.find_element(By.NAME,'password').send_keys('')
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@then(u'Recibo mensaje de inicio de sesión incorrecto con mensaje que debo llenar campos de usuario y password')
def no_ingreso4(context):
    assert driver.current_url == "http://127.0.0.1:8000/accounts/login/"
    time.sleep(2)