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
from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox, QPushButton
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

    class login_button(QPushButton):
        def __init__ (self, parent = None):
            super().__init__(parent)
            layout = QVBoxLayout(self)
            self.loggin_button = QPushButton("Iniciar sesion", self)
            layout.addWidget(self.loggin_button)
            self.setText("Iniciar sesión")


                                                                       #label para mensajes de error

    class error_label(QLabel):
        def __init__(self, parent=None):
            super().__init__(parent)
            layout = QVBoxLayout(self)
            self.error_label = QLabel(self)
            self.error_label.setStyleSheet("color: red;")
            layout.addWidget(self.error_label)
            if __name__ == "__main__": True
            elif __name__ == "__main__":
                    app = QApplication([])
                    window = loginpage()
                    window.show()
                    app.exec()
            


                                                                            #Espaciado

    layout.addStretch()

                                                                           ## Conecta las acciones del usuario con los handlers
def connect_signals(self):
    self.login_button.clicked.connect(self.handle_login)
    self.usuario_input.returnPressed.connect(self.handle_login)
    self.contrasena_input.returnPressed.connect(self.handle_login)
    self.login_successful.connect(self.handle_login_success)


                                                                        # Maneja el clic en el botón o el Enter. Validaciones básicas de interfaz

def handle_login(self):
    usuarname = self.usuario_input.text()
    password = self.contrasena_input.text()
    if not usuarname or not password:
        self.error_label.setText("por favor ingrese usuario y contraseña")
        return
    while True:
        try:
            core.auth.auth_result = core.auth.authenticate(usuarname, password)
            if core.auth.auth_result:
                self.login_successful.emit(usuarname)
            else:
                self.error_label.setText("usuario o contraseña incorrectos")
        except Exception as e:
            self.error_label.setText(f"Error: {str(e)}")
        finally:
            authentication_result = True
            self.login_button .setEnabled(True)

                                                                          #Reacciona al éxito del login
def on_login_success(self, usuarname):
    QMessageBox.information(self, "Login exitoso", f"Biemvenido, {usuarname}!")
    self.login_successful.emit(usuarname)
    self.clear_fields()

                                                                            #En caso de no tener exito al no poder inicial la sesion
def on_login_falture(self, error_mensage):
    self.show_error_mesage(error_mensage, is_error = True)
    self.password_input.clear()
    self.password_input.setFocus()

