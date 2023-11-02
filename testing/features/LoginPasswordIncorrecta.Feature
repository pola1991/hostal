Feature: Ingreso de usuario al sistema
Scenario: Inicio de sesion incorrecto (Contraseña)
    Given Accedo a la url para hacer login con contraseña incorrecta "http://127.0.0.1:8000/"
    When hago click en enlace para hacer inicio de sesion con contraseña incorrecta "//*[@id="navbarNavDropdown"]/ul/li[3]/a"
    And Ingresa las credenciales de acceso con contraseña incorrecta
    Then Recibo mensaje inicio de sesion incorrecto (Contraseña)
