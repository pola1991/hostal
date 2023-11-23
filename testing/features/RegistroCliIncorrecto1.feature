Feature: No ingresar al formulario el usuario   
Scenario: Registro incorrecto (Usuario en blanco)
    Given Accedo a la url para registrar cliente con usuario en blanco "http://127.0.0.1:8000/"
    When Hago click en enlace para registrar cliente con usuario en blanco "//*[@id='navbarNavDropdown']/ul/li[4]/a"
    And Ingreso todos los demas datos dejando usuario en blanco
    Then Registro de cliente incorrecto con mensaje para ingresar usuario