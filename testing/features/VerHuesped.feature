Feature: Ver administracion de huespedes hostal
Scenario: Administracion de huespedes
    Given Ingreso a home para posteriormente ver huespedes "http://127.0.0.1:8000/"
    When Hago click para loguearme con permisos para ver huespedes "linkIniciarSesion"
    And Ingresa con permisos para ver huespedes
    And Ingreso exitoso con permisos respectivos para ver huespedes
    And Hago click en reservas para luego ver huespedes "reservas"
    And Hago click en enlace para ver huespedes "verHuespedes"
    Then Puedo ver los huespedes "http://127.0.0.1:8000/huespedes"