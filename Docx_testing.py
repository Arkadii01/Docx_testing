import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import docx_worker
import json

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn_save.clicked.connect(self.save)
        self.btn_load.clicked.connect(self.load)
        
    def save(self):
        pass
    
    def load(self):
        pass
        
if __name__ == '__main__':
    MainWidget().show()
    sys.exit(QApplication(sys.argv).exec())