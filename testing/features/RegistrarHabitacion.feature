Feature: Registro de habitacion como secretaria
Scenario: Registrar habitacion
    Given Ingreso a la url index "http://127.0.0.1:8000/"
    When Hago click y me logueo como secretaria "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Ingreso credenciales de secretaria
    And Ingreso exitoso secretaria
    And Hago click en el enlace reservas "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Hago click en enlace para registrar habitaciones "//*[@id="navbarNavDropdown"]/ul[1]/li[3]/ul/li[3]/a"
    And Ingreso datos al formulario de registro de habitaciones
    Then Se registran la habitacion