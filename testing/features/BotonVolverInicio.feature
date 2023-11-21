Feature: Prueba boton volver inicio
Scenario: Prueba boton volver a inicio
    Given Accedo a la url para darle clik a boton inicio de sesion y luego volver a inicio "http://127.0.0.1:8000/"
    When Hago click en enlace de inicio de sesion y luego volver a inicio "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    When Logro ingresar a la pagina de inicio de sesion
    When Hago clik en boton volver inicio "/html/body/div/div/div/div/div[2]/form/div[3]/a"
    Then Me redireccionara a home