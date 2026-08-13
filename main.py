#Este es el iniciador de todo, depende de login_page.py para que siga, es el iniciador, no hace nada mas
from PySide6.QtWidgets import QApplication, QWidget
from ui.pages.login_page import loginwindow
window = loginwindow()
app = QApplication()
widget = QWidget()
widget.show()
app.exec()