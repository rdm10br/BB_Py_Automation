from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QWidget, QGridLayout, QMessageBox, QProgressBar)
from PySide6.QtCore import Qt, QTimer, QThread, Signal, QSize
from PySide6.QtGui import QIcon, QCursor, QFontDatabase, QMovie
import subprocess, sys, setproctitle, os, json
from functools import lru_cache

@lru_cache
class Worker(QThread):
    finished = Signal(str)
    message_box_signal = Signal(str)
    progress_updated = Signal(int)
    

    def __init__(self, script_path):
        super().__init__()
        self.script_path = script_path
        self.main_window = MainWindow()
        self.p = None
    
    def run(self):
        try:
            print(f'Trying to run process: {self.script_path}')
            setproctitle.setproctitle(f"MyApp: {self.script_path}")
            env = os.environ.copy()
            env["PYTHONUNBUFFERED"] = "1"
            
            self.progress_updated.emit(0)
            
            if self.script_path == r'src\Metodos\Login\getCredentials.py':
                
                script_dir = os.path.dirname(os.path.abspath(__file__))
                src_dir = os.path.join(script_dir, 'src')
                if src_dir not in sys.path:
                    sys.path.insert(0, src_dir)
                
                from Metodos.Login.getCredentials import get_credentials
                
                username, password = get_credentials()
                
                self.finished.emit(f'{username},{password}')
                
            else:
                process = subprocess.Popen([r"venv\Scripts\python.exe", self.script_path],
                                bufsize=1)
                
                # for line in iter(process.stdout.readline, ''):
                #     print(line.strip())
                #     progress = self.parse_progress_from_output(line.strip())
                #     self.progress_updated.emit(progress)
                    
                # process.stdout.close()
                process.wait()
                
                self.finished.emit(f"Finished running {self.script_path}")
        except FileNotFoundError as e:
            self.finished.emit(f"Error running subprocess: {e}")

@lru_cache
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_stylesheet(r"src\style\style.qss")
        self.setWindowTitle("Project Main Interface")
        self.setMinimumSize(900, 500)
        self.setWindowIcon(QIcon(r'src\style\icon\automation0.png'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        font_id = QFontDatabase.addApplicationFont(r"src\font\Poppins\Poppins-Regular.ttf")
        if font_id == -1:
            ...
        else:
            ...

        font_families = QFontDatabase.applicationFontFamilies(font_id)
        for family in font_families:
            ...
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        self.loading_label = QLabel()
        self.loading_label.setFixedSize(60, 60)
        self.loading_movie = QMovie(r'src\style\icon\work-in-progress.gif')
        self.loading_movie.setScaledSize(QSize(60, 60))
        self.loading_label.setMovie(self.loading_movie)
        self.loading_label.setObjectName('load')
        layout.addWidget(self.loading_label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        self.loading_label.hide()
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(30)
        self.progress_bar.setFixedWidth(700)
        layout.addWidget(self.progress_bar, 1, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.hide()
        
        label = QLabel("Escolha o Robô que você quer utilizar:")
        label.setObjectName('textChoice')
        layout.addWidget(label, 3, 0, 1, 2)
        
        button_module2 = QPushButton("Criação de BQ")
        button_module2.clicked.connect(lambda: self.run_module(r"src\Main_BQ.py"))
        layout.addWidget(button_module2, 4, 0, 1, 2)
        
        button_module3 = QPushButton("Copia de Material")
        button_module3.clicked.connect(lambda: self.run_module(r"src\Main_copy_material.py"))
        layout.addWidget(button_module3, 5, 0)
        
        button_module4 = QPushButton("Copia de Sala")
        button_module4.clicked.connect(lambda: self.run_module(r"src\Main_copy_sala.py"))
        layout.addWidget(button_module4, 5, 1)
        
        button_module5 = QPushButton("DoubleCheck Master")
        button_module5.clicked.connect(lambda: self.run_module(r"src\Main_doublecheck_Master.py"))
        layout.addWidget(button_module5, 7, 0)
        
        button_module6 = QPushButton("DoubleCheck Mescla DIG")
        button_module6.clicked.connect(lambda: self.run_module(r"src\Main_doubleCheck_Mescla_DIG.py"))
        layout.addWidget(button_module6, 7, 1)
        
        button_module1 = QPushButton("DoubleCheck Configurações de Itens")
        button_module1.setObjectName('button_2')
        button_module1.clicked.connect(lambda: self.run_module(r"src\Main_config_doublecheck.py"))
        layout.addWidget(button_module1, 8, 0)
        
        button_module6 = QPushButton("DoubleCheck Mescla VET")
        button_module6.clicked.connect(lambda: self.run_module(r"src\Main_doublecheck_Mescla_VET.py"))
        layout.addWidget(button_module6, 8, 1, 1, 1)
        
        button_module7 = QPushButton("Atividades Praticas")
        button_module7.clicked.connect(lambda: self.run_module(r"src\Main_ATividades_Praticas.py"))
        layout.addWidget(button_module7, 6, 0)
        
        button_module8 = QPushButton("Ajuste de Datas")
        button_module8.clicked.connect(lambda: self.run_module(r"src\Main_ajusteData.py"))
        layout.addWidget(button_module8, 6, 1)
        
        button_exit = QPushButton("Save credentials")
        button_exit.clicked.connect(lambda: self.run_module(r'src\Metodos\Login\getCredentials.py'))
        button_exit.setObjectName('save_button')
        layout.addWidget(button_exit, 9, 0, 1, 2)
        
        button_exit = QPushButton("Delete credentials")
        button_exit.clicked.connect(self.delete_cache)
        button_exit.setObjectName('delete_button')
        layout.addWidget(button_exit, 10, 0, 1, 2)
        
        button_module9 = QPushButton("Check")
        button_module9.clicked.connect(lambda: self.run_module(r"src\Main_Test.py"))
        button_module9.setObjectName('ButtonTest')
        layout.addWidget(button_module9, 11, 0, 1, 2)

        
        QTimer.singleShot(0, self.center_window)
        
        self.username = None
        self.password = None
        
    def save_to_cache(self):
        cache_file = os.path.join(os.path.curdir, r'src\Metodos\Login\__pycache__\login.json')
        username = self.username
        password = self.password
        
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
        self.progress_bar.show()
        self.loading_label.show()
        self.loading_movie.start()
        
        self.thread: Worker = Worker(script_path)
        self.thread.finished.connect(self.on_finished)
        self.thread.message_box_signal.connect(self.display_message_box)
        self.thread.progress_updated.connect(self.update_progress_bar)
        self.thread.start()

    def on_finished(self, message: str):
        if message.startswith("Error"):
            QMessageBox.critical(self, 'Error 01', message)
            self.progress_bar.hide()
            self.loading_movie.stop()
            self.loading_label.hide()
        elif self.thread.script_path == r'src\Metodos\Login\getCredentials.py':
            credentials = message.split(',')
            if len(credentials) == 2:
                self.username, self.password = credentials
                self.save_to_cache()
                self.progress_bar.hide()
                self.loading_movie.stop()
                self.loading_label.hide()
            else:
                QMessageBox.critical(self, 'Error 02', 'Invalid credentials format.')
                self.progress_bar.hide()
                self.loading_movie.stop()
                self.loading_label.hide()
        else:
            print(message)
            self.progress_bar.hide()
            self.loading_movie.stop()
            self.loading_label.hide()
            
    def display_message_box(self, message: str, icon=QMessageBox.Information):
        QMessageBox.information(self, 'Information', message, QMessageBox.Ok, QMessageBox.NoButton)
    
    def update_progress_bar(self, percent):
        self.progress_bar.setValue(percent)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()