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
from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox, QPushButton
                               , QLineEdit, QLabel, QHBoxLayout, QVBoxLayout) 

import PySide6.QtCore
from PySide6.QtCore import Signal

# ui/login_page.py
class LoginPage:
    def __init__(self, auth):  #Recibe auth, no lo importa
        self.auth = auth


class loginpage (QWidget):
    login_successful = Signal (object)

    def __init__ (self,parent = None):
        super().__init__(parent)
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        layout = QVBoxLayout(self)
                                                                    #Titulo de la ventana
        title = QLabel ("Iniciar sesion")
        title.setAlignment(PySide6.QtCore.Qt.AlignCenter)
        layout.addWidget(title)
                                                                    #campo de usuario
        self.usuario_input = QLineEdit(self)
        self.usuario_input.setPlaceholderText ("Usuario")
        layout.addWidget(self.usuario_input)
                                                                    #campo de contraseña
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Iniciar sesión", self)
        layout.addWidget(self.login_button)
                                                                       #label para mensajes de error
        self.error_label = QLabel(self)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.hide()
        layout.addWidget(self.error_label)
                                                                            #Espaciado, Conecta las acciones del usuario con los handlers
        layout.addStretch()

    def connect_signals(self):
        self.login_button.clicked.connect(self.handle_login)
        self.usuario_input.returnPressed.connect(self.handle_login)
        self.password_input.returnPressed.connect(self.handle_login)

    def handle_login(self):
        username = self.usuario_input.text()
        password = self.password_input.text()
        if not username:
            self.error_label.setText("Por favor, ingrese su usuario.")
            self.error_label.show()
            return
        if not password:
            self.error_label.setText("Por favor, ingrese su contraseña.")
            self.error_label.show()
            return
        self.error_label.hide()
        success, message = self.auth.authenticate_user(username, password)
        if success: 
            self.successful_login(username)
        else:
            self.on_login_failure(message)

    def clear_fields(self):
            self.usuario_input.clear()
            self.password_input.clear()
            self.usuario_input.setFocus()
    
    def successful_login(self, username):
        QMessageBox.information(self, "Login exitoso", f"Bienvenido, {username}!")
        self.login_successful.emit(username)
        self.handle_login_success()
        

                                                                            #En caso de no tener exito al no poder inicial la sesion
    def on_login_failure(self, error_message):
        self.clear_fields()
        self.error_label.setText(error_message)
        self.error_label.show()

if __name__ == "__main__": 
    app = QApplication([])
    window = loginpage()
    window.show()
    app.exec()