Feature: Ingreso de usuario al sistema
Scenario: Inicio de sesion
    Given Accedo a la url http://127.0.0.1:8000/accounts/login/
    When Localiza enlace "Iniciar Sesion"
    And Ingresa las credenciales de acceso
    Then Ingresa a la cuenta
