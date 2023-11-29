Feature: Eliminar proveedor del sistema
Scenario: Gestionar proveedores
    Given Accedo a direccion http "http://127.0.0.1:8000/"
    When Hago click en loguearme "linkIniciarSesion"
    And Ingresa las credencial
    And Ingreso con exito a cuenta
    And Hago click reservar "reservas"
    And Hago click en enlace para añadir nuevo proveedor "registrarProveedor"
    And añado nuevo proveedor
    And Hago click reservar otra vez "reservas"
    And Hago click en enlace para ver proveedor "verProveedor"
    And Hago click en boton eliminar "//*[@id='contenido']/div/table/tbody/tr[1]/td[6]/a"
    And Confirmacion "/html/body/h2"
    Then puedo ver proveedor borrado "http://127.0.0.1:8000/readProveedor/"