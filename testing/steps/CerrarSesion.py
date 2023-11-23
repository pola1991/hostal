from behave import given,when,then
from selenium.webdriver.common.by import By
from conexion import webapp

driver = webapp.get_driver()
@given(u'Ingreso a la url para hacer inicio de sesion "{url}"')
def step_acceso_a_la_url(context,url):
    driver.get(url)
    driver.maximize_window()

@when(u'Ingreso las credenciales e ingreso a la cuenta')
def ingresa_credenciales(context):
    driver.find_element(By.XPATH,"//*[@id='id_username']").clear()
    driver.find_element(By.XPATH,"//*[@id='id_username']").send_keys("paula")
    driver.find_element(By.NAME,'password').send_keys('paula')
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

@when(u'Apreto el link para cerrar sesion')
def apreto_link_para_cerrar_sesion(context):
    driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul[1]/li[4]/a").click()

@then(u'Regreso al home page con la sesion cerrada')
def regreso_con_sesion_cerrada(context):
    if(driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul/li[3]/a").is_displayed()):
        print('Cierre de sesion correcto')
    else:
        print('Cierre de sesion fallido')