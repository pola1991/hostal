from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()


@given(u'Accedo a la url para hacer login con usuario en blanco "{url}"')
def acceso(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace para hacer inicio de sesion con usuario en blanco "{link}"')
def localizador(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()
    

@when(u'Ingreso solo password dejando usuario en blanco')
def ingresa_solo_password(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("")
    driver.find_element(By.NAME,'password').send_keys('paula')
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@then(u'Recibo mensaje de inicio de sesión incorrecto con mensaje para ingresar usuario')
def no_ingreso(context):
    if(driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[1]").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')