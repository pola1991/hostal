Feature: Registro de cliente
Scenario: Registro de 1 cliente
    Given Accedo a la url index para luego registrar cliente "http://127.0.0.1:8000/"
    When Hago click en enlace para registrarme como cliente "//*[@id='navbarNavDropdown']/ul/li[4]/a"
    And Completo formulario cliente
    Then Se registra el cliente