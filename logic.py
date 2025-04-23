from PyQt6.QtWidgets import *
from gui import Ui_MainWindow

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)