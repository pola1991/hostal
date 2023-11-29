from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webapp.get_driver()

@given(u'Ingreso a la url index "{url}"')
def acceso_a_la_url7(context, url):
    driver.get("http://127.0.0.1:8000/accounts/logout/")
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click y me logueo como secretaria "{link}"')
def localiza_enl_login7(context, link):
    driver.find_element(By.ID, link).click()

@when(u'Ingreso credenciales de secretaria')
def ingresa_credenciales_secretaria7(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()
    
@when(u'Ingreso exitoso secretaria')
def ingresa_a_la_cuenta7(context):
    assert driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()

@when(u'Hago click en el enlace reservas "{link}"')
def hago_click_en_boton_reserva7(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()


@when(u'Hago click en enlace para registrar habitaciones "{link}"')
def hago_click_en_enlace_add_habitacion(context, link):
    time.sleep(1)
    driver.find_element(By.ID, "registrarHabitacion").click()


@when(u'Ingreso datos al formulario de registro de habitaciones')
def ingreso_datos_formulario_registro_habitacion(context):
    driver.find_element(By.XPATH, "//*[@id='id_n_habitacion']").send_keys(234)
    driver.find_element(By.XPATH, "//*[@id='id_nombre']").send_keys("Pasta de dientes")
    driver.find_element(By.XPATH, "//*[@id='id_precio']").send_keys(92119123)
    driver.find_element(By.XPATH, "//*[@id='id_n_camas']").send_keys(2)
    driver.find_element(By.XPATH, "//*[@id='id_descripcion']").send_keys("N/A")
    time.sleep(1)
    driver.execute_script('document.querySelector("#contenido > div > div > form > button").click()')

@then(u'Se registran la habitacion')
def se_registra_la_habitacion(context):
    driver.get("http://127.0.0.1:8000/hab")
    assert driver.find_element(By.XPATH, "//*[@id='contenido']/div/table/tbody/tr/th[1]").is_displayed()
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/accounts/logout/")