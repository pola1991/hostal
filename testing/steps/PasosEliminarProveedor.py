from behave import given, when, then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()


@given(u'Accedo a direccion http "{url}"')
def url(context, url):
    driver.get(url)

@when(u'Hago click en loguearme "{link}"')
def localiza_enlace(context, link):
    #//*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, link).click()

@when(u'Ingresa las credencial')
def credenciales(context):
    driver.find_element(By.XPATH, "//*[@id='id_username']").clear()
    driver.find_element(By.XPATH, "//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME, 'password').send_keys('paula')
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@when(u'Ingreso con exito a cuenta')
def ingreso_cuenta(context):
    if driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed():
        print('login correcto')
    else:
        print('login fallido')

@when(u'Hago click reservar "{link}"')
def presiono_reserva(context, link):
    driver.find_element(By.XPATH, link).click()


@when(u'Hago click en enlace para ver proveedor "{link}"')
def hago_click_en_enlace_ver_proveedores(context, link):
    driver.find_element(By.ID, "verProveedor").click()



@when(u'Veo los proveedores "{url}"')
def see_proveedores(context, url):
    driver.get(url)
        
@when(u'Hago click en boton eliminar "{link}"')
def hago_click_en_enlace_eliminar_proveedores(context, link):
    driver.find_element(By.XPATH, "//*[@id='contenido']/div/table/tbody/tr[1]/td[6]/a").click()

@when(u'Confirmacion "{link}"')
def confirmacion_eliminar_proveedor(context, link):
    driver.find_element(By.XPATH, "/html/body/form/input[2]").click()
   

@then(u'puedo ver proveedor borrado"{url}"')
def puedo_ver_proveedores(context,url):
    driver.implicitly_wait(20000)
    driver.get(url)