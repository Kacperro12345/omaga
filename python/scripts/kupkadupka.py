import PySide6
from PySide6 import QtCore

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# Główne okno
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja pierwsza aplikacja w PySide6")  # tytuł okna
        self.setGeometry(100, 100, 400, 300)  # pozycja x, y, szerokość, wysokość

        # Przykładowy label
        label = QLabel("Siema, to PySide6 działa!", self)
        label.setGeometry(50, 50, 200, 40)  # ustawiamy prostokąt (x, y, szer, wys)

# Standardowy boilerplate
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
