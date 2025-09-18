import PySide6
from PySide6 import QtCore

import sys
from PySide6.QtWidgets import *

# Główne okno
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Omaga")
        self.setGeometry(750, 400, 400, 300)

        self.kupy = 0

        self.label = QLabel(f"Kupa: {self.kupy}", self)
        self.label.setGeometry(150, 50, 60, 15)
        self.label.setStyleSheet("""
            color: #7085c4;
        """)

        button = QPushButton("Kupa", self)
        button.setGeometry(150, 200, 100, 40)
        button.clicked.connect(self.on_click)

    def on_click(self):
        self.kupy += 1
        self.label.setText(f"Kupy: {self.kupy}")

# Standardowy boilerplate
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
