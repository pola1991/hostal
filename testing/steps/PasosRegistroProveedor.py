from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()

@given(u'Accedo a la url index "{url}"')
def acceso_a_la_url(context, url):
    driver.get("http://127.0.0.1:8000/accounts/logout/")
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace para loguearme como secretaria "{link}"')
def localiza_enl_login(context, link):
    driver.implicitly_wait(5)
    driver.find_element(By.ID, link).click()

@when(u'Ingresa las credenciales de acceso secretaria')
def ingresa_credenciales_secretaria(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@when(u'Logro ingresar a la cuenta como secretaria')
def ingresa_a_la_cuenta(context):
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()

@when(u'Hago click en reserva "{link}"')
def hago_click_en_boton_reserva(context, link):
    time.sleep(3)
    driver.find_element(By.ID, link).click()

@when(u'Hago click en enlace para registrar proveedores "{link}"')
def hago_click_en_enlace_ver_proveedores(context, link):
    time.sleep(3)
    driver.find_element(By.ID, link).click()

@when(u'Ingreso datos al formulario de registro de proveedores')
def ingreso_datos_formulario_registro_proveedores(context):
    driver.find_element(By.XPATH, "//*[@id='id_nombre']").send_keys("Rosen")
    driver.find_element(By.XPATH, "//*[@id='id_rubro']").send_keys("Camas")
    driver.find_element(By.XPATH, "//*[@id='id_contacto']").send_keys(92119123)
    driver.find_element(By.XPATH, " //*[@id='id_otro']").send_keys("N/A")
    driver.implicitly_wait(5)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='btnAgregarProveedor']").submit()

@then(u'Se registran los proveedores')
def se_registran_los_proveedores(context):
    assert driver.find_element(By.XPATH, "//*[@id='contenido']/div/div/div[1]/div[2]/h4").is_displayed()
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/accounts/logout/")