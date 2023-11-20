Feature: Registro de proveedor al sistema
Scenario: Registro de proveedor
    Given Accedo a la url index "http://127.0.0.1:8000/"
    When Hago click en enlace para loguearme como secretaria "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Ingresa las credenciales de acceso secretaria
    And Logro ingresar a la cuenta como secretaria
    And Hago click en reserva "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Hago click en enlace para registrar proveedores "#registrarProveedor"
    And Ingreso datos al formulario de registro de proveedores 
    Then Se registran los proveedores 
