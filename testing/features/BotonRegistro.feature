Feature: Ingreso al sistema para ingresar a registrar
Scenario: Prueba boton registrar
    Given Accedo a la url para darle clik a boton registrar "http://127.0.0.1:8000/"
    When hago click en enlace de registrarse "linkRegistroCliente"
    Then Puedo ingresar a la pagina de registro