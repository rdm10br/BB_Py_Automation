from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
import sys, time
from threads_test_ui import Ui_MainWindow  # Import the generated UI file

class Main_Threads(QMainWindow):
    def __init__(self):
        super(Main_Threads, self).__init__()
        self.ui = Ui_MainWindow()  # Instantiate the UI
        self.ui.setupUi(self)  # Set up the UI

        # self.resize(310, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r'C:\Users\013190873\Downloads\Pessoal\VS\BB_Py_Automation\src\icon\automated-process.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        self.pushButton = self.ui.pushButton
        # self.pushButton_2 = self.ui.pushButton_2
        # self.pushButton_3 = self.ui.pushButton_3
        # self.pushButton_4 = self.ui.pushButton_4
        # self.pushButton_5 = self.ui.pushButton_5
        # self.pushButton_6 = self.ui.pushButton_6
        self.progressBar = self.ui.progressBar
        # self.progressBar_2 = self.ui.progressBar_2
        # self.progressBar_3 = self.ui.progressBar_3
        
        self.thread = {}
        self.pushButton.clicked.connect(self.start_worker_1)
        # self.pushButton_2.clicked.connect(self.start_worker_2)
        # self.pushButton_3.clicked.connect(self.start_worker_3)
        # self.pushButton_4.clicked.connect(self.stop_worker_1)
        # self.pushButton_6.clicked.connect(self.stop_worker_2)
        # self.pushButton_5.clicked.connect(self.stop_worker_3)
    
    def start_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].any_signal.connect(self.my_function)
        self.thread[1].start()
        self.pushButton.setEnabled(False)
        # self.pushButton_4.setEnabled(True)
    
    def start_worker_2(self):
        self.thread[2] = ThreadClass(parent=None, index=2)
        self.thread[2].any_signal.connect(self.my_function)
        self.thread[2].start()
        self.pushButton_2.setEnabled(False)
        self.pushButton_6.setEnabled(True)
        
    def start_worker_3(self):
        self.thread[3] = ThreadClass(parent=None, index=3)
        self.thread[3].any_signal.connect(self.my_function)
        self.thread[3].start()
        self.pushButton_3.setEnabled(False)
        self.pushButton_5.setEnabled(True)
    
    def stop_worker_1(self):
        self.thread[1].stop()
        self.pushButton.setEnabled(True)
        self.pushButton_4.setEnabled(False)
    
    def stop_worker_2(self):
        self.thread[2].stop()
        self.pushButton_2.setEnabled(True)
        self.pushButton_6.setEnabled(False)
    
    def stop_worker_3(self):
        self.thread[3].stop()
        self.pushButton_3.setEnabled(True)
        self.pushButton_5.setEnabled(False)
        
    def my_function(self, counter):
        cnt = counter
        index = self.sender().index
        if index == 1:
            self.progressBar.setValue(cnt)
        elif index == 2:
            self.progressBar_2.setValue(cnt)
        elif index == 3:
            self.progressBar_3.setValue(cnt)

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.Signal(int)
    
    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True
    
    def run(self):
        print('Starting Thread...', self.index)
        cnt = 0
        while self.is_running and cnt <= 100:
            cnt += 1
            time.sleep(0.1)
            self.any_signal.emit(cnt)
        print('Exiting Thread...', self.index)
    
    def stop(self):
        self.is_running = False
        self.wait()  # Wait for the thread to finish

def Main():
    app = QApplication(sys.argv)
    mainWindow = Main_Threads()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    Main()
