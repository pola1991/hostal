from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()


@given(u'Accedo direccion http "{url}"')
def url(context, url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click para loguearme como secretaria "{link}"')
def localiza_enlace(context, link):
    #//*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.ID, link).click()

@when(u'Digita credenciales')
def credenciales(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@when(u'Ingreso con exito cuenta')
def ingreso_cuenta(context):
    if driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed():
        print('login correcto')
    else:
        print('login fallido')

@when(u'Selecciono haciendo click en reservas "{link}"')
def presiono_reserva(context, link):
    driver.find_element(By.ID, link).click()


@when(u'Hago click en enlace para ver platos "{link}"')
def hago_click_en_enlace_ver_platos(context, link):
    driver.find_element(By.ID, "verPlatos").click()



@when(u'Veo los platos "{url}"')
def see_platos(context, url):
    driver.get(url)
        
@when(u'Hago click en boton eliminar platos "{link}"')
def hago_click_en_enlace_eliminar_plato(context, link):
    driver.find_element(By.XPATH, "//*[@id='contenido']/div/table/tbody/tr[1]/td[5]/a").click()

   

@when(u'Hago click en Confirmacion')
def confirmacion_eliminar_plato(context):
    driver.find_element(By.XPATH, "/html/body/form/input[2]").click()
   

@then(u'puedo ver el plato borrado "{url}"')
def puedo_ver_platos(context,url):
    driver.implicitly_wait(20000)
    driver.get(url)
    driver.find_element(By.ID,"linkCerrarSesion").click()