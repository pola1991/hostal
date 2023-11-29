Feature: Ver perfil
Scenario:Ver perfil
    Given Accedo a la url home "http://127.0.0.1:8000/"
    When Hago click en enlace de inicio de sesión "linkIniciarSesion"
    And Ingresa credenciales de acceso 
    And Puedo ingresar a mi cuenta
    Then Hago click en ver perfil propio "linkPerfilCliente"