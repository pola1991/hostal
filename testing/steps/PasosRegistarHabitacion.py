from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webapp.get_driver()


@given(u'Ingreso a la url index "{url}"')
def acceso_a_la_url7(context, url):
    driver.get(url)


@when(u'Hago click y me logueo como secretaria "{link}"')
def localiza_enl_login7(context, link):
    # //*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, link).click()


@when(u'Ingreso credenciales de secretaria')
def ingresa_credenciales_secretaria7(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()
    

@when(u'Ingreso exitoso secretaria')
def ingresa_a_la_cuenta7(context):
    driver.implicitly_wait(5)
    if(driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')


@when(u'Hago click en el enlace reservas "{link}"')
def hago_click_en_boton_reserva7(context, link):
    driver.find_element(By.XPATH, link).click()


@when(u'Hago click en enlace para registrar habitaciones "{link}"')
def hago_click_en_enlace_add_habitacion(context, link):
    driver.find_element(By.ID, "registrarHabitacion").click()


@when(u'Ingreso datos al formulario de registro de habitaciones')
def ingreso_datos_formulario_registro_habitacion(context):
    driver.find_element(By.XPATH, "//*[@id='id_n_habitacion']").send_keys(234)
    driver.find_element(By.XPATH, "//*[@id='id_nombre']").send_keys("Pasta de dientes")
    driver.find_element(By.XPATH, "//*[@id='id_precio']").send_keys(92119123)
    driver.find_element(By.XPATH, "//*[@id='id_n_camas']").send_keys(2)
    driver.find_element(By.XPATH, "//*[@id='id_descripcion']").send_keys("N/A")

    # Espera a que el elemento 'id_estado_habitacion' sea clicle y luego haz clic en él
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_estado_habitacion']")))
    element.click()

    driver.implicitly_wait(5)

    # Selecciona una opción del dropdown
    element_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_estado_habitacion']/option[2]")))
    element_option.click()

    driver.implicitly_wait(5)
    
    driver.find_element(By.XPATH, "//*[@id='contenido']/div/div/form/button").submit()

@then(u'Se registran la habitacion')
def se_registra_la_habitacion(context):
    if(driver.find_element(By.XPATH, "//*[@id='contenido']/div/table/tbody/tr/th[1]").is_displayed()):
        print('Registro correcto')
    else:
        print('Registro fallido')