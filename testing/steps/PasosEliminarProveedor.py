from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webapp.get_driver()
wait = WebDriverWait(driver, 20)

@given(u'Accedo a direccion http "{url}"')
def url(context, url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en loguearme "{link}"')
def localiza_enlace(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()

@when(u'Ingresa las credencial')
def credenciales(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    time.sleep(1)
    driver.find_element(By.ID, "loginBtn").click()

@when(u'Ingreso con exito a cuenta')
def ingreso_cuenta(context):
    assert driver.find_element(By.ID, "linkCerrarSesion").is_displayed()

@when(u'Hago click reservar "{link}"')
def presiono_reserva(context, link):
    driver.find_element(By.ID, link).click()

@when(u'Hago click en enlace para añadir nuevo proveedor "{link}"')
def hago_click_en_enlace_agregar_proveedores(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()

@when(u'añado nuevo proveedor')
def add_proveedores(context):
    driver.find_element(By.XPATH, "//*[@id='id_nombre']").send_keys("Proveedor de prueba")
    driver.find_element(By.XPATH, "//*[@id='id_rubro']").send_keys("Comida")
    driver.find_element(By.XPATH, "//*[@id='id_contacto']").send_keys('965236325')
    driver.find_element(By.XPATH, "//*[@id='id_otro']").send_keys('prueba')
    driver.execute_script('document.querySelector("#btnAgregarProveedor").click()')
    assert driver.find_element(By.XPATH, "//*[@id='contenido']/div/div/div[1]/div[2]/h4").is_displayed()

@when(u'Hago click reservar otra vez "{link}"')
def presiono_reserva2(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()

@when(u'Hago click en enlace para ver proveedor "{link}"')
def hago_click_en_enlace_ver_proveedores2(context, link):
    time.sleep(1)
    driver.find_element(By.ID, link).click()
        
@when(u'Hago click en boton eliminar "{link}"')
def hago_click_en_enlace_eliminar_proveedores(context, link):
    driver.find_element(By.XPATH, link).click()

@when(u'Confirmacion "{link}"')
def confirmacion_eliminar_proveedor(context, link):
    time.sleep(1)
    assert driver.find_element(By.XPATH, link).is_displayed()
    driver.find_element(By.XPATH, "/html/body/form/input[2]").click()
   
@then(u'puedo ver proveedor borrado "{url}"')
def puedo_ver_proveedores(context,url):
    assert driver.current_url == "http://127.0.0.1:8000/readProveedor/"
    driver.find_element(By.ID,"linkCerrarSesion").click()