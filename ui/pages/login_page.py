#Para login_page.py conviene que trabajes solo la parte de interfaz y coordinación del login, no la autenticación criptográfica ni SQL.
#Definir qué responsabilidad tendrá la página
#1 Crear la clase principal de la página de login.
#2 mostrar los campos;
#3 recibir las acciones del usuario;
#4 validar condiciones básicas de la interfaz;
#5 llamar a core.auth;
#6 reaccionar al resultado;
#7 mostrar mensajes al usuario;
#8 informar a la aplicación cuando el login fue exitoso.
#9 No colocar dentro de esta página:
#10 consultas SQL;
#11 generación de hashes de contraseñas;
#12 generación de salts;
#13 comparación criptográfica de contraseñas;
#14 creación de usuarios directamente en SQLite.
import PySide6.Qt.lib
from PySide6.QtWidgets import (QWidget, QMessageBox, QPushButton
                               , QLineEdit, QLabel, QHBoxLayout, QVBoxLayout) 

import PySide6.QtCore
import signal, abc
import core.auth

class loginpage (QWidget):
    login_successful = signal (object)

    def __init__ (self,parent = None):
        super().__init__(parent)
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        layout = QVBoxLayout (layout)
#Titulo de la ventana
        title = QLabel ("Iniciar sesion")
        title.setAlignment(PySide6.QtCore.Qt.AlignCenter)
        layout.addWidget(title)
#campo de usuario
        self.usuario_input = QLineEdit(self)

    self = any.input
    layout = QVBoxLayout(self)
    self.usuario_input.setPlaceholderText ("Usuario")
    layout.addWidget(self.usuario_input)
#campo de contraseña

    class contraseña_input(QLineEdit):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setPlaceholderText("Contraseña")
            self.setEchoMode(QLineEdit.Password)
            layout = QVBoxLayout(self)
            self.contrasena_input = QLineEdit(self)
            self.contrasena_input.setPlaceholderText("Contraseña")
            self.contrasena_input.setEchoMode(QLineEdit.Password)
            layout.addWidget(self.contrasena_input)

#boton de login

#label para mensajes de error

#Espaciado

