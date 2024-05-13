from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webapp.get_driver()


@given(u'Ingreso a la url index9 "{url}"')
def acceso_a_la_url9(context, url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click y me logueo como secretaria9 "{link}"')
def localiza_enl_login9(context, link):
    driver.implicitly_wait(5)
    driver.find_element(By.ID, link).click()


@when(u'Ingreso credenciales de secretaria9')
def ingresa_credenciales_secretaria9(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()
    

@when(u'Ingreso exitoso secretaria9')
def ingresa_a_la_cuenta9(context):
    driver.implicitly_wait(5)
    if(driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')


@when(u'Hago click en el enlace reservas9 "{link}"')
def hago_click_en_boton_reserva9(context, link):
    driver.find_element(By.ID, link).click()


@when(u'Hago click en enlace para registrar plato')
def hago_click_en_enlace_ver_plato(context):
    driver.find_element(By.ID, "registrarComedor").click()


@when(u'Ingreso datos al formulario de registro platos')
def ingreso_datos_formulario_registro_platos(context):
    driver.find_element(By.XPATH, "//*[@id='id_nombre_plato']").send_keys("Tortilla de verduras")
    driver.find_element(By.XPATH, "//*[@id='id_precio']").send_keys(15000)
    
    # Espera a que el elemento 'id_estado_habitacion' sea clicle y luego haz clic en él
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_servicio_comedor']")))
    element.click()

    driver.implicitly_wait(5)

    # Selecciona una opción del dropdown
    element_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_servicio_comedor']/option[2]")))
    element_option.click()

    driver.implicitly_wait(5)


    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//*[@id='btnAgregarPlato']").submit()


@then(u'Se registra el plato')
def se_registra_plato(context):
    if(driver.find_element(By.XPATH, "//*[@id='contenido']/div/div/div[1]/div[2]/h4").is_displayed()):
        print('Registro correcto')
    else:
        print('Registro fallido')
    driver.find_element(By.ID,"linkCerrarSesion").click()
