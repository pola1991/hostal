Feature: Ingresar usuario con valores numéricos
Scenario: Inicio de sesion incorrecto (Solo ingreso de usuario numerico)
    Given Accedo a la url para hacer login con usuario numerico "http://127.0.0.1:8000/"
    When Hago click en enlace para hacer inicio de sesion con usuario numerico "//*[@id="navbarNavDropdown"]/ul/li[3]/a"
    And Ingreso solo usuario numerico
    Then Recibo mensaje de inicio de sesión incorrecto con mensaje que debo llenar campos