from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
import sys, time
from src.style.Main_UI_ui import Ui_MainWindow

class Main_UI():
    def __init__(self):
        super(Main_UI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
def Main():
    app = QApplication(sys.argv)
    mainWindow = Main_UI()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    Main()