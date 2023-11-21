Feature: Ingreso al sistema para ingresar a inicio de sesion
Scenario: Prueba boton inicio de sesion
    Given Accedo a la url para darle clik a boton inicio de sesion "http://127.0.0.1:8000/"
    When Hago click en enlace de inicio de sesion "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    Then Puedo ingresar a la pagina de inicio de sesion