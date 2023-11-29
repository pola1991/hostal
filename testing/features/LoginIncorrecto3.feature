Feature: Ingresar usuario con valores numéricos
Scenario: Inicio de sesion incorrecto (Dejando en blanco password)
    Given Accedo a la url para hacer login con password en blanco "http://127.0.0.1:8000/"
    When Hago click en enlace para hacer inicio de sesion con password en blanco "linkIniciarSesion"
    And Ingreso solo usuario dejando password en blanco
    Then Recibo mensaje de inicio de sesión incorrecto con mensaje que debo llenar campos de password