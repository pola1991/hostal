Feature: Registro de plato
Scenario: Registrar plato
    Given Ingreso a la url index9 "http://127.0.0.1:8000/"
    When Hago click y me logueo como secretaria9 "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Ingreso credenciales de secretaria9
    And Ingreso exitoso secretaria9
    And Hago click en el enlace reservas9 "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Hago click en enlace para registrar plato
    And Ingreso datos al formulario de registro platos
    Then Se registra el plato