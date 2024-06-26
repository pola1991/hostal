from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()
@given(u'Accedo a la url "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'hago click en enlace "{link}"')
def localiza_enlace_login(context,link):
    time.sleep(2)
    driver.find_element(By.ID,link).click()
    
@when(u'Ingresa las credenciales de acceso')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME,'password').send_keys('paula')
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@then(u'Puedo ingresar a la cuenta')
def ingresa_a_la_cuenta(context):
    assert driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()
    time.sleep(2)
    driver.find_element(By.ID,"linkCerrarSesion").click()