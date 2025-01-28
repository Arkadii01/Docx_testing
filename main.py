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
        self.btn_main.clicked.connect(self.get_main)
        self.btn_text.clicked.connect(self.get_text)
        self.btn_void.clicked.connect(self.get_void)
        self.btn_element.clicked.connect(self.get_element)
        self.btn_content.clicked.connect(self.get_content)
        self.btn_load.clicked.connect(self.load)
        os.chdir('data')
        with open('data.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        os.chdir('../docs_for_test')
        for file in os.listdir():
            self.box_filename.addItem(file)
        os.chdir('..')
        self.box_filetype.setCurrentText(self.data['filetype'])
        self.input_teacher.appendPlainText(self.data['teacher'])
        self.edgewall_up.setValue(self.data['edge-wall']['top'])
        self.edgewall_bottom.setValue(self.data['edge-wall']['bottom'])
        self.edgewall_left.setValue(self.data['edge-wall']['left'])
        self.edgewall_right.setValue(self.data['edge-wall']['right'])
        self.walltext_up.setValue(self.data['wall-text']['top'])
        self.walltext_bottom.setValue(self.data['wall-text']['bottom'])
        self.walltext_left.setValue(self.data['wall-text']['left'])
        self.walltext_right.setValue(self.data['wall-text']['right'])
        self.fontsize.setValue(self.data['font-size'])
        self.rows_distance.setValue(self.data['rows_distance'])
        self.first_void.setValue(self.data['first_void'])

    def update(self):
        self.close()
        self.text_error.hide()
        self.text_success.hide()
        self.show()
        
    def get_main(self):
        pass
    
    def get_main(self):
        self.close()
        uic.loadUi('data//main.ui')
        self.show()

    def get_text(self):
        self.close()
        uic.loadUi('data//main.ui')
        self.show()
        
    def save(self):
        self.data['filetype'] = self.box_filetype.currentText()
        self.data['filename'] = self.box_filename.currentText()
        self.data['teacher'] = self.input_teacher.toPlainText()
        self.data['edge-wall']['top'] = self.edgewall_up.value()
        self.data['edge-wall']['left'] = self.edgewall_left.value()
        self.data['edge-wall']['right'] = self.edgewall_right.value()
        self.data['edge-wall']['bottom'] = self.edgewall_bottom.value()
        self.data['wall-text']['top'] = self.walltext_up.value()
        self.data['wall-text']['left'] = self.walltext_left.value()
        self.data['wall-text']['right'] = self.walltext_right.value()
        self.data['wall-text']['bottom'] = self.walltext_bottom.value()
        self.data['font-size'] = self.fontsize.value()
        self.data['rows_distance'] = self.rows_distance.value()
        self.data['first_void'] = self.first_void.value()
        print(self.data)
        os.chdir('data')
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent='  ')
        os.chdir('..')
    
    def load(self):
        try:
            docx_worker.docx_fixer()
        except Exception as ex:
            print(ex)
            self.update()
            self.text_error.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MainWidget()
    wid.show()
    sys.exit(app.exec())