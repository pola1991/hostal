Feature: Ingreso de usuario al sistema
Scenario: Inicio de sesion
    Given Accedo a la url "http://127.0.0.1:8000/"
    When hago click en enlace "//*[@id="navbarNavDropdown"]/ul/li[3]/a"
    And Ingresa las credenciales de acceso
    Then Puedo ingresar a la cuenta
