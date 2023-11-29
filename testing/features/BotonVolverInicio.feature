Feature: Prueba boton volver inicio
Scenario: Prueba boton volver a inicio
    Given Accedo a la url para darle clik a boton inicio de sesion y luego volver a inicio "http://127.0.0.1:8000/"
    When Hago click en enlace de inicio de sesion y luego volver a inicio "linkIniciarSesion"
    When Logro ingresar a la pagina de inicio de sesion
    When Hago clik en boton volver inicio "volverInicio"
    Then Me redireccionara a home