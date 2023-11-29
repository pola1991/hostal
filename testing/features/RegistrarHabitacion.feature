Feature: Registro de habitacion como secretaria
Scenario: Registrar habitacion
    Given Ingreso a la url index "http://127.0.0.1:8000/"
    When Hago click y me logueo como secretaria "linkIniciarSesion"
    And Ingreso credenciales de secretaria
    And Ingreso exitoso secretaria
    And Hago click en el enlace reservas "reservas"
    And Hago click en enlace para registrar habitaciones "registrarHabitacion"
    And Ingreso datos al formulario de registro de habitaciones
    Then Se registran la habitacion