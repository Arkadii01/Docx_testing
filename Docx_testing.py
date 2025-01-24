import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        
if __name__ == '__main__':
    MainWidget().show()
    sys.exit(QApplication(sys.argv).exec())
