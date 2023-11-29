Feature: Ver Poveedor
Scenario: Ver Proveedor
    Given Accedo a la url de home "http://127.0.0.1:8000/"
    When Hago click en enlace para loguearme "linkIniciarSesion"
    And Ingresa las credenciales de acceso de secretaria
    And Puedo ingresar a la cuenta como secretaria
    And Hago click en el boton reserva "reservas"
    And Hago click en enlace para ver proveedores "verProveedor"
    Then Puedo ver los proveedores "http://127.0.0.1:8000/readProveedor/"