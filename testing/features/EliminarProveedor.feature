Feature: Eliminar proveedor del sistema
Scenario: Gestionar proveedores
    Given Accedo a direccion http "http://127.0.0.1:8000/"
    When Hago click en loguearme "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Ingresa las credencial
    And Ingreso con exito a cuenta
    And Hago click reservar "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Hago click en enlace para ver proveedor "#verProveedor"
    And Veo los proveedores "http://127.0.0.1:8000/readProveedor/"
    And Hago click en boton eliminar "//*[@id='contenido']/div/table/tbody/tr[1]/td[6]/a"
    And Confirmacion "/html/body/h2"
    Then puedo ver proveedor borrado "http://127.0.0.1:8000/readProveedor/"