Feature: Ingreso de usuario al sistema
Scenario: Inicio de sesion incorrecto
    Given Accedo a la url para hacer login incorrecto "http://127.0.0.1:8000/"
    When hago click en enlace para hacer inicio de sesion incorrecto "//*[@id="navbarNavDropdown"]/ul/li[3]/a"
    And Ingresa las credenciales de acceso incorrecto
    Then Recibo mensaje inicio de sesion incorrecto
