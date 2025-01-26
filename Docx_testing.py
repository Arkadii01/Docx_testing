import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
import docx_worker
import json
import os

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data//main.ui', self)
        self.text_success.hide()
        self.text_error.hide()
        self.btn_save.clicked.connect(self.save)
        self.btn_load.clicked.connect(self.load)
        os.chdir('data')
        with open('data.json', 'r', encoding='utf-8') as file:
            text = ''.join(file.readlines())[1:]
            data = json.loads(text)
        os.chdir('../docs_for_test')
        for file in os.listdir():
            self.box_filename.addItem(file)
        self.box_filetype.setCurrentText(data['filetype'])
        self.input_teacher.appendPlainText(data['teacher'])
        self.edgewall_up.setValue(data['edge-wall']['top'])
        self.edgewall_bottom.setValue(data['edge-wall']['bottom'])
        self.edgewall_left.setValue(data['edge-wall']['left'])
        self.edgewall_right.setValue(data['edge-wall']['right'])
        self.walltext_up.setValue(data['wall-text']['top'])
        self.walltext_bottom.setValue(data['wall-text']['bottom'])
        self.walltext_left.setValue(data['wall-text']['left'])
        self.walltext_right.setValue(data['wall-text']['right'])
        self.fontsize.setValue(data['font-size'])
        self.rows_distance.setValue(data['rows_distance'])
        self.first_void.setValue(data['first_void'])

    def update(self):
        self.close()
        self.show()
        
    def save(self):
        print(self.edgewall_up.value())
        print(self.box_filename.currentText())
    
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