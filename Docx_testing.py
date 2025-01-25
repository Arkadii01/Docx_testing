import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import docx_worker
import json

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data//main.ui', self)
        self.text_success.hide()
        self.text_error.hide()
        self.btn_save.clicked.connect(self.save)
        self.btn_load.clicked.connect(self.load)

    def update(self):
        self.close()
        self.show()
        
    def save(self):
        pass
    
    def load(self):
        try:
            pass
        except Exception as ex:
            print(ex)
            self.text_error.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MainWidget()
    wid.show()
    sys.exit(app.exec())