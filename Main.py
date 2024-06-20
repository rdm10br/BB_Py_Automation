from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QPushButton, QWidget, QGridLayout)
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtGui import QIcon, QCursor
import subprocess, sys, setproctitle


class Worker(QThread):
    finished = Signal(str)

    def __init__(self, script_path):
        super().__init__()
        self.script_path = script_path

    def run(self):
        try:
            setproctitle.setproctitle(f"MyApp: {self.script_path}")  # Set custom process name
            subprocess.run([r"venv\Scripts\python.exe", self.script_path])
            self.finished.emit(f"Finished running {self.script_path}")
        except FileNotFoundError as e:
            self.finished.emit(f"Error running subprocess: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_stylesheet(r"src\style\style.qss")
        self.setWindowTitle("Project Main Interface")
        self.setMinimumSize(510, 300)
        self.setWindowIcon(QIcon(r'src\icon\automation.png'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        label = QLabel("Escolha a o Robô que você quer utilizar:")
        label.setObjectName('textChoice')
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label, 0, 0, 1, 2)
        
        button_module1 = QPushButton("DoubleCheck Configurações de Itens")
        button_module1.clicked.connect(lambda: self.run_module(r"src\Main_config_doublecheck.py"))
        layout.addWidget(button_module1, 1, 0)

        button_module2 = QPushButton("Criação de BQ")
        button_module2.clicked.connect(lambda: self.run_module(r"src\Main_BQ.py"))
        layout.addWidget(button_module2, 1, 1)
        
        button_module3 = QPushButton("Copia de Material")
        button_module3.clicked.connect(lambda: self.run_module(r"src\Main_copy_material.py"))
        layout.addWidget(button_module3, 2, 0)
        
        button_module4 = QPushButton("Copia de Sala")
        button_module1.setObjectName('button_2')
        button_module4.clicked.connect(lambda: self.run_module(r"src\Main_copy_sala.py"))
        layout.addWidget(button_module4, 2, 1)
        
        button_module5 = QPushButton("DoubleCheck Master")
        button_module5.clicked.connect(lambda: self.run_module(r"src\Main_doublecheck_Master.py"))
        layout.addWidget(button_module5, 3, 0)
        
        button_module6 = QPushButton("DoubleCheck Mescla")
        button_module6.clicked.connect(lambda: self.run_module(r"src\Main_doubleCheck_Mescla.py"))
        layout.addWidget(button_module6, 3, 1)
        
        button_module7 = QPushButton("Atividades Praticas")
        button_module7.clicked.connect(lambda: self.run_module(r"src\Main_ATividades_Praticas.py"))
        layout.addWidget(button_module7, 4, 0)
        
        button_module8 = QPushButton("Ajuste de Datas")
        button_module8.clicked.connect(lambda: self.run_module(r"src\Main_ajusteData.py"))
        layout.addWidget(button_module8, 4, 1)
        
        button_module9 = QPushButton("Check")
        button_module9.clicked.connect(lambda: self.run_module(r"src\Main_Test.py"))
        button_module9.setObjectName('ButtonTest')
        layout.addWidget(button_module9, 5, 0, 1, 2)

        button_exit = QPushButton("Sair")
        button_exit.clicked.connect(self.close)
        button_exit.setObjectName('exitButton')
        layout.addWidget(button_exit, 6, 0, 1, 2)
        
        QTimer.singleShot(0, self.center_window)
    
    def load_stylesheet(self, file_name):
        with open(file_name, "r") as file:
            self.setStyleSheet(file.read())
        
    def center_window(self):
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        if screen:
            screen_geometry = screen.geometry()
            window_geometry = self.frameGeometry()
            x = screen_geometry.x() + (screen_geometry.width() - window_geometry.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - window_geometry.height()) // 2
            self.move(x, y)

    def run_module(self, script_path):
        self.thread = Worker(script_path)
        self.thread.finished.connect(self.on_finished)
        self.thread.start()

    def on_finished(self, message):
        print(message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
