from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()


@given(u'Ingreso a home para posteriormente ver huespedes "{url}"')
def acceso_a_la_url9(context, url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click para loguearme con permisos para ver huespedes "{link}"')
def localiza_enl_login9(context, link):
    driver.implicitly_wait(5)
    driver.find_element(By.ID, link).click()


@when(u'Ingresa con permisos para ver huespedes')
def ingresa_credenciales_secretaria9(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()
    

@when(u'Ingreso exitoso con permisos respectivos para ver huespedes')
def ingresa_a_la_cuenta9(context):
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()

@when(u'Hago click en reservas para luego ver huespedes "{link}"')
def hago_click_en_boton_reserva9(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()


@when(u'Hago click en enlace para ver huespedes "{link}"')
def hago_click_en_enlace_ver_huespedes(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()


@then(u'Puedo ver los huespedes "{url}"')
def veo_huespedes(context,url):
    assert driver.current_url == url
    time.sleep(2)
    driver.find_element(By.ID,"linkCerrarSesion").click()
        

