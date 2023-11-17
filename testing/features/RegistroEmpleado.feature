Feature: Registro de empleado
Scenario: Registro de un empleado
    Given Accedo a la url index para luegon registrar empleado "http://127.0.0.1:8000/"
    When Hago click en enlace y me logueo como secretaria "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Ingreso credenciales de acceso secretaria
    And Me logueo exitosamente como secretaria
    And Hago click en reservas "//*[@id='navbarNavDropdown']/ul/li[3]/a"
    And Hago click en enlace para registrar empleado "//*[@id="navbarNavDropdown"]/ul[1]/li[3]/ul/li[1]/a"
    And Completo formulario empleado
    Then Se registra el empleado