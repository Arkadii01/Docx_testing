import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit

class ContentWidget(QMainWindow):
    def __init__(self):
        super().__init__
        uic.loadUi('data//content.ui')
        