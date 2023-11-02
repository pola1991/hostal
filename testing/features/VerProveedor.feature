Feature: Ingreso de usuario al sistema
Scenario: Inicio de sesion
    Given Accedo a la url de home "http://127.0.0.1:8000/"
    When Hago click en enlace para loguearme "//*[@id="navbarNavDropdown"]/ul/li[3]/a"
    And Ingresa las credenciales de acceso de secretaria
    And Puedo ingresar a la cuenta como secretaria
    And Hago click en el boton reserva "//*[@id="navbarNavDropdown"]/ul[1]/li[3]/a"
    And Hago click en enlace para ver proveedores "#verProveedor"
    Then Puedo ver los proveedores "http://127.0.0.1:8000/readProveedor/"

    
