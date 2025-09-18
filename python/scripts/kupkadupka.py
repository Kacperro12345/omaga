import PySide6
from PySide6 import QtCore

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# Główne okno
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Omaga")
        self.setGeometry(750, 400, 400, 300)

        Label = QLabel("Kupa", self)
        Label.setGeometry(150, 75, 100, 100)

# Standardowy boilerplate
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
