from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()


@given(u'Accedo a la url de home "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get("http://127.0.0.1:8000/accounts/logout/")
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace para loguearme "{link}"')
def localiza_enlace_login(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.ID,link).click()

@when(u'Ingresa las credenciales de acceso de secretaria')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME,'password').send_keys('paula')
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()


@when(u'Puedo ingresar a la cuenta como secretaria')
def ingresa_a_la_cuenta(context):
    if(driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')


@when(u'Hago click en el boton reserva "{link}"')
def hago_click_en_boton_reserva(context, link):
    driver.find_element(By.ID, link).click()


@when(u'Hago click en enlace para ver proveedores "{link}"')
def hago_click_en_enlace_ver_proveedores(context, link):
    driver.find_element(By.ID, link).click()


@then(u'Puedo ver los proveedores "{url}"')
def veo_proveedores(context,url):
    assert driver.current_url == url
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/accounts/logout/")
        
