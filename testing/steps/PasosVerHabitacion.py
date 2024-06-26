from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()


@given(u'Ingreso a home para posteriormente ver habitaciones "{url}"')
def acceso_a_la_url8(context, url):
    driver.get(url)
    driver.maximize_window()


@when(u'Hago click para loguearme con permisos para ver habitaciones "{link}"')
def localiza_enl_login8(context, link):
    driver.implicitly_wait(5)
    time.sleep(1)
    driver.find_element(By.ID, link).click()


@when(u'Ingresa con permisos para ver habitaciones')
def ingresa_credenciales_secretaria8(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()
    

@when(u'Ingreso exitoso con permisos respectivos para ver habitaciones')
def ingresa_a_la_cuenta8(context):
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()

@when(u'Hago click en reservas para luego ver habitaciones "{link}"')
def hago_click_en_boton_reserva8(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()


@when(u'Hago click en enlace para ver habitaciones disponibles')
def hago_click_en_enlace_ver_platos(context):
    time.sleep(1)
    driver.find_element(By.ID, "verHabitaciones").click()


@then(u'Puedo ver los habitaciones disponibles "{url}"')
def veo_platos(context,url):
    assert driver.current_url == "http://127.0.0.1:8000/hab"
    time.sleep(2)
    driver.find_element(By.ID,"linkCerrarSesion").click()
        

