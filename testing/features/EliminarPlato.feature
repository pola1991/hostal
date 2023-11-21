Feature: Eliminar plato del sistema
Scenario: Gestionar proveedores
    Given Accedo direccion http "http://127.0.0.1:8000/"
    When Hago click para loguearme como secretaria "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Digita credenciales
    And Ingreso con exito cuenta
    And Selecciono haciendo click en reservas "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Hago click en enlace para ver platos "#verPlatos"
    And Veo los platos "http://127.0.0.1:8000/readComedor/"
    And Hago click en boton eliminar platos "//*[@id="contenido"]/div/table/tbody/tr[3]/td[5]/a"
    And Hago click en Confirmacion 
    Then puedo ver el plato borrado "http://127.0.0.1:8000/readComedor/"