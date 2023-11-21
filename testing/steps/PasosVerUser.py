from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()

@given(u'Accedo a la url home "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Hago click en enlace de inicio de sesión "{link}"')
def localiza_enlace_login(context,link):
    #//*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()
    

@when(u'Ingresa credenciales de acceso')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME,'password').send_keys('paula')
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

    

@when(u'Puedo ingresar a mi cuenta')
def ingresa_a_la_cuenta(context):
    if(driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')

@then(u'Hago click en ver perfil propio "{link}"')
def veo_perfil(context,link):
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,link).click()