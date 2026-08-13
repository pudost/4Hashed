from PySide6.QtWidgets import QApplication, QWidget
from ui.pages.login_page import loginwindow
window = loginwindow()
app = QApplication()
widget = QWidget()
widget.show()
app.exec()