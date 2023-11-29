Feature: Ver administracion de platos hostal
Scenario: Administracion de platos
    Given Ingreso a home "http://127.0.0.1:8000/"
    When Hago click para loguearme "linkIniciarSesion"
    And Ingresa como secretaria
    And Ingreso exitoso como una secretaria
    And Hago click en el boton reservas "reservas"
    And Hago click en enlace para ver platos disponibles "verPlatos"
    Then Puedo ver los platos disponibles "http://127.0.0.1:8000/readComedor/"