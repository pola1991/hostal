Feature: Ver administracion de habitaciones hostal
Scenario: Administracion de habitaciones
    Given Ingreso a home para posteriormente ver habitaciones "http://127.0.0.1:8000/"
    When Hago click para loguearme con permisos para ver habitaciones "//*[@id="navbarNavDropdown"]/ul/li[3]/a"
    And Ingresa con permisos para ver habitaciones
    And Ingreso exitoso con permisos respectivos para ver habitaciones
    And Hago click en reservas para luego ver habitaciones "//*[@id="navbarNavDropdown"]/ul[1]/li[3]/a"
    And Hago click en enlace para ver habitaciones disponibles
    Then Puedo ver los habitaciones disponibles "http://127.0.0.1:8000/hab"
