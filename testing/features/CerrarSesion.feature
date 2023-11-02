Feature: Cierre de sesion del sistema
Scenario: Cerrar sesion
    Given Ingreso a la url para hacer inicio de sesion "http://127.0.0.1:8000/accounts/login/"
    When Ingreso las credenciales e ingreso a la cuenta
    And Apreto el link para cerrar sesion
    Then Regreso al home page con la sesion cerrada
