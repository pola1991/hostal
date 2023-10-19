from behave import given,when,then
from webapp import webapp

driver = webapp.get_driver()
@given('Acceso a la url "{url}"')
def step_acceso_a_la_url(context,url)
    driver.get('http://127.0.0.1:8000/accounts/login/')

@when('Localiza enlace iniciar sesion "{link}"')
def localiza_enlace_login(context,link)
    driver.find_element_by_link_text(link).click()
    driver.implicitly_wait(5)

@when('Ingresa credenciales')
def ingresa_credenciales(context)
    driver.find_element_by_xpath("//*[@id='usuario']").clear()
    driver.find_element_by_xpath("//*[@id='usuario']").send_keys("paula")
    driver.find_element_by_name('password').send_keys('12345678')
    driver.find_element_by_name('enviar').click()

@then('ingresa a la cuenta')