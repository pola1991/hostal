from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()


@given(u'Accedo a la url para hacer login con password en blanco "{url}"')
def acceso1(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace para hacer inicio de sesion con password en blanco "{link}"')
def localizador1(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()
    

@when(u'Ingreso solo password dejando password en blanco')
def ingresa_solo_usuario(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME,'password').send_keys('')
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@then(u'Recibo mensaje de inicio de sesión incorrecto con mensaje que debo llenar campos de password')
def no_ingreso1(context):
    if(driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[1]").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')