from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
import time

driver = webapp.get_driver()


@given(u'Accedo a la url index para luego registrar cliente "{url}"')
def acceso_a_la_url6(context, url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace para registrarme como cliente "{link}"')
def hago_click_en_enlace_registrar(context, link):
    driver.find_element(By.ID, link).click()


@when(u'Completo formulario cliente')
def ingreso_datos_formulario_registro_cliente(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("Samsung_sur")
    driver.find_element(By.XPATH, "//*[@id='id_nombre_empresa']").send_keys("Samsung")
    driver.find_element(By.XPATH, "//*[@id='id_rut_empresa']").send_keys("100.223.234-3")
    driver.find_element(By.XPATH, "//*[@id='id_email']").send_keys("samsung@gmail.com")
    driver.find_element(By.XPATH, "//*[@id='id_password1']").send_keys("Felipe8.")
    driver.find_element(By.XPATH, "//*[@id='id_password2']").send_keys("Felipe8.")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[7]/input").submit()
    

@then(u'Se registra el cliente')
def se_registran_los_clientes(context):
    assert driver.find_element(By.XPATH, "//*[@id='linkPerfilCliente']").is_displayed()
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/delete_last_user/")


