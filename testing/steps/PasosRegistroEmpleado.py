from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
import time
driver = webapp.get_driver()

@given(u'Accedo a la url index para luegon registrar empleado "{url}"')
def acceso_a_la_url(context, url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace y me logueo como secretaria "{link}"')
def localiza_enl_login(context, link):
    # //*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.ID, link).click()

@when(u'Ingreso credenciales de acceso secretaria')
def ingresa_credenciales_secretaria(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()
    
@when(u'Me logueo exitosamente como secretaria')
def ingresa_a_la_cuenta(context):
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()

@when(u'Hago click en reservas "{link}"')
def hago_click_en_boton_reserva(context, link):
    driver.find_element(By.ID, link).click()

@when(u'Hago click en enlace para registrar empleado "{link}"')
def hago_click_en_enlace_registrar(context, link):
    driver.find_element(By.ID, link).click()

@when(u'Completo formulario empleado')
def ingreso_datos_formulario_registro_empleado(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("Rayyy")
    driver.find_element(By.XPATH, "//*[@id='id_first_name']").send_keys("Raymond")
    driver.find_element(By.XPATH, "//*[@id='id_last_name']").send_keys("Durkin")
    driver.find_element(By.XPATH, "//*[@id='id_cargo']").send_keys("Asesor")
    driver.find_element(By.XPATH, "//*[@id='id_email']").send_keys("Durkin@gmail.com")
    driver.find_element(By.XPATH, "//*[@id='id_password1']").send_keys("Paulita7.")
    driver.find_element(By.XPATH, "//*[@id='id_password2']").send_keys("Paulita7.")
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[8]/input").submit()
    
@then(u'Se registra el empleado')
def se_registran_los_clientes(context):
    assert driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/delete_last_user/")