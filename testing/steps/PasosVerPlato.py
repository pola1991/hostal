from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()


@given(u'Ingreso a home "{url}"')
def acceso_a_la_url8(context, url):
    driver.get(url)
    driver.maximize_window()


@when(u'Hago click para loguearme "{link}"')
def localiza_enl_login8(context, link):
    driver.implicitly_wait(5)
    driver.find_element(By.ID, link).click()


@when(u'Ingresa como secretaria')
def ingresa_credenciales_secretaria8(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()
    

@when(u'Ingreso exitoso como una secretaria')
def ingresa_a_la_cuenta8(context):
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()


@when(u'Hago click en el boton reservas "{link}"')
def hago_click_en_boton_reserva8(context, link):
    driver.find_element(By.ID, link).click()


@when(u'Hago click en enlace para ver platos disponibles "{link}"')
def hago_click_en_enlace_ver_platos(context, link):
    time.sleep(2)
    driver.find_element(By.ID, link).click()


@then(u'Puedo ver los platos disponibles "{url}"')
def veo_platos(context,url):
    assert driver.current_url == url
    time.sleep(2)
    driver.find_element(By.ID,"linkCerrarSesion").click()


