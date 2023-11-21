from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp



driver = webapp.get_driver()
@given(u'Accedo a la url para darle clik a boton inicio de sesion y luego volver a inicio "{url}"')
def step_acceso_a_la_url5(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace de inicio de sesion y luego volver a inicio "{link}"')
def localiza_enlace_logi5(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()
    
@when(u'Logro ingresar a la pagina de inicio de sesion')
def ingresa_a_la_cuenta(context):
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[1]/h3").click
    
@when(u'Hago clik en boton volver inicio "{link}"')
def localiza_enlace(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()


@then(u'Me redireccionara a home')
def regreso_con_sesion_cerrada(context):
    if(driver.find_element(By.XPATH,"//*[@id=\'carouselExampleIndicators\']/div[2]/div[2]/img").is_displayed()):
        print('Redireccion correcta')
    else:
        print('Redireccion fallida')