from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()

@given(u'Accedo a la url home "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get("http://127.0.0.1:8000/accounts/logout/")
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace de inicio de sesión "{link}"')
def localiza_enlace_login(context,link):
    #//*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.ID,link).click()
    

@when(u'Ingresa credenciales de acceso')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME,'password').send_keys('paula')
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

    

@when(u'Puedo ingresar a mi cuenta')
def ingresa_a_la_cuenta(context):
    assert driver.find_element(By.XPATH,"//*[@id='linkCerrarSesion']").is_displayed()

@then(u'Hago click en ver perfil propio "{link}"')
def veo_perfil(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.ID,link).click()

    assert driver.current_url == "http://127.0.0.1:8000/perfilCliente/"
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/accounts/logout/")