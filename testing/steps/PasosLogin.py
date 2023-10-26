from behave import given,when,then
from conexion import webapp

driver = webapp.get_driver()
@given(u'Accedo a la url "{url}"')
def step_acceso_a_la_url(context,url):
    #http://127.0.0.1:8000/accounts/login/
    driver.get(url)

@when(u'hago click en enlace "{link}"')
def localiza_enlace_login(context,link):
    #//*[@id="navbarNavDropdown"]/ul/li[3]/a
    driver.find_element_by_xpath(link).click()
    driver.implicitly_wait(5)

@when(u'Ingresa las credenciales de acceso')
def ingresa_credenciales(context):
    driver.find_element_by_xpath("//*[@id='id_username']").clear()
    driver.find_element_by_xpath("//*[@id='id_username']").send_keys("paula")
    driver.find_element_by_name('password').send_keys('12345678')
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[3]/input").click()

    

@then(u'Puedo ingresar a la cuenta')
def ingresa_a_la_cuenta(context):
    if(driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul[2]/li/a").is_displayed()):
        print('login correcto')
    else:
        print('login fallido')