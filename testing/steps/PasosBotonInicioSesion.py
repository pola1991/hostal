from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()
@given(u'Accedo a la url para darle clik a boton inicio de sesion "{url}"')
def step_acceso_a_la_url5(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace de inicio de sesion "{link}"')
def localiza_enlace_logi5(context,link):
    #//*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()
    
@then(u'Puedo ingresar a la pagina de inicio de sesion')
def ingresa_a_la_cuenta(context):
    if(driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[1]/h3").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')