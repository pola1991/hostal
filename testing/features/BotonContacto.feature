Feature: Ingreso al sistema para ingresar a boton contacto
Scenario: Prueba boton contacto
    Given Accedo a la url para darle clik a boton contacto "http://127.0.0.1:8000/"
    When Hago click en enlace de contacto "botonContactoMenu"
    Then Me redirecciona al apartado de contacto