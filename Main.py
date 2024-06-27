from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QPushButton, QWidget, QGridLayout, QMessageBox)
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QIcon, QCursor, QFontDatabase
import subprocess, sys, setproctitle, os, json


class Worker(QThread):
    finished = Signal(str)

    def __init__(self, script_path):
        super().__init__()
        self.script_path = script_path

    def run(self):
        try:
            print(f'Trying to run process: {self.script_path}')
            # self.started.emit(f'Trying to run process: {self.script_path}')
            setproctitle.setproctitle(f"MyApp: {self.script_path}")  # Set custom process name
            if self.script_path == r'src\Metodos\Login\getCredentials.py':
                script_dir = os.path.dirname(os.path.abspath(__file__))
                src_dir = os.path.join(script_dir, 'src')
                if src_dir not in sys.path:
                    sys.path.insert(0, src_dir)
                
                from Metodos.Login.getCredentials import get_credentials
                username, password = get_credentials()
                self.finished.emit(f'{username},{password}')
            else:
                subprocess.run([r"venv\Scripts\python.exe", self.script_path])
                self.finished.emit(f"Finished running {self.script_path}")
        except FileNotFoundError as e:
            self.finished.emit(f"Error running subprocess: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_stylesheet(r"src\style\style.qss")
        self.setWindowTitle("Project Main Interface")
        self.setMinimumSize(900, 500)
        self.setWindowIcon(QIcon(r'src\icon\automation0.png'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        font_id = QFontDatabase.addApplicationFont(r"src\font\Poppins\Poppins-Regular.ttf")
        if font_id == -1:
            # print("Failed to load font.")
            ...
        else:
            # print("Font loaded successfully.")
            ...

        # List available fonts
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        for family in font_families:
            # print("Available font family:", family)
            ...
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        label = QLabel("Escolha a o Robô que você quer utilizar:")
        label.setObjectName('textChoice')
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
        
        button_exit = QPushButton("Save credentials")
        button_exit.clicked.connect(lambda: self.run_module(r'src\Metodos\Login\getCredentials.py'))
        button_exit.setObjectName('save_button')
        layout.addWidget(button_exit, 5, 0)
        
        button_exit = QPushButton("Delete credentials")
        button_exit.clicked.connect(self.delete_cache)
        button_exit.setObjectName('delete_button')
        layout.addWidget(button_exit, 5, 1)
        
        button_module9 = QPushButton("Check")
        button_module9.clicked.connect(lambda: self.run_module(r"src\Main_Test.py"))
        button_module9.setObjectName('ButtonTest')
        layout.addWidget(button_module9, 6, 0, 1, 2)

        
        QTimer.singleShot(0, self.center_window)
        
        self.username = None
        self.password = None
        
    def save_to_cache(self):
        # Define the cache file path
        # cache_file = os.path.join(os.path.expanduser('~'), r'src\Metodos\Login\__pycache__\login.json')
        cache_file = os.path.join(os.path.curdir, r'src\Metodos\Login\__pycache__\login.json')
        # Information to be cached
        username = self.username
        password = self.password

        # Information to be cached
        cache_info = {
            "username": username,
            "password": password
        }

        try:
            with open(cache_file, 'w') as file:
                json.dump(cache_info, file, indent=4)
            QMessageBox.information(self, 'Success', 'Information saved to cache.')
            print(f"Finished running {self.thread.script_path}")
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save to cache: {e}')
    
    def delete_cache(self):
        # Define the cache file path
        cache_file = os.path.join(os.path.curdir, r'src\Metodos\Login\__pycache__\login.json')

        try:
            if os.path.exists(cache_file):
                os.remove(cache_file)
                QMessageBox.information(self, 'Success', 'Cache file deleted.')
            else:
                QMessageBox.information(self, 'Info', 'No cache file found.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to delete cache file: {e}')
    
    def load_stylesheet(self, file_name):
        with open(file_name, "r") as file:
            self.setStyleSheet(file.read())
            
        # variables = {
        #     'background': 'rgba(1, 8, 22, 1)',
        #     'foreground': 'rgba(247, 249, 251, 1)',
        #     'card': 'rgba(1, 8, 22, 1)',
        #     'card-foreground': 'rgba(247, 249, 251, 1)',
        #     'popover': 'rgba(1, 8, 22, 1)',
        #     'popover-foreground': 'rgba(247, 249, 251, 1)',
        #     'primary': 'rgba(59, 130, 245, 1)',
        #     'primary-foreground': 'rgba(15, 23, 42, 1)',
        #     'secondary': 'rgba(30, 41, 59, 1)',
        #     'secondary-foreground': 'rgba(247, 249, 251, 1)',
        #     'muted': 'rgba(30, 41, 59, 1)',
        #     'muted-foreground': 'rgba(148, 163, 183, 1)',
        #     'accent': 'rgba(30, 41, 59, 1)',
        #     'accent-foreground': 'rgba(247, 249, 251, 1)',
        #     'destructive': 'rgba(127, 29, 29, 1)',
        #     'destructive-foreground': 'rgba(247, 249, 251, 1)',
        #     'border': 'rgba(30, 41, 59, 1)',
        #     'input': 'rgba(30, 41, 59, 1)',
        #     'ring': 'rgba(29, 77, 215, 1)'
        # }
        # with open(file_name, 'r') as file:
        #     qss_template = file.read()
        # for key, value in variables.items():
        #     qss_template = qss_template.replace(f'{{{{ {key} }}}}', value)
        # self.setStyleSheet(qss_template)
        
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
        self.thread: Worker = Worker(script_path)
        self.thread.finished.connect(self.on_finished)
        # self.thread.started.connect(self.on_started)
        self.thread.start()

    def on_finished(self, message: str):
        if message.startswith("Error"):
            QMessageBox.critical(self, 'Error 01', message)
        elif self.thread.script_path == r'src\Metodos\Login\getCredentials.py':
            credentials = message.split(',')
            if len(credentials) == 2:
                self.username, self.password = credentials
                self.save_to_cache()
            else:
                QMessageBox.critical(self, 'Error 02', 'Invalid credentials format.')
        else:
            print(message)
            
    def on_started(self, message: str):
        print(message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()