Feature: Ingreso de usuario al sistema
Scenario: Inicio de sesion incorrecto (Usuario)
    Given Accedo a la url para hacer login con usuario incorrecto "http://127.0.0.1:8000/"
    When hago click en enlace para hacer inicio de sesion con usuario incorrecto "linkIniciarSesion"
    And Ingresa las credenciales de acceso con usuario incorrecto
    Then Recibo mensaje inicio de sesion incorrecto (usuario)
