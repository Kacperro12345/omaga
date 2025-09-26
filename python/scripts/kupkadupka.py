import PySide6
from PySide6 import QtCore

import sys
from PySide6.QtWidgets import *

# Główne okno
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Omaga kalkulejtor")
        self.setGeometry(750, 400, 320, 500)

        self.layout = QGridLayout()

        btn1 = QPushButton("1")




# Standardowy boilerplate
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
