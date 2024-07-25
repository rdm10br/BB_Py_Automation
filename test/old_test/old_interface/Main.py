from PySide6 import QtCore, QtGui
from PySide6.QtGui import QCursor
from PySide6.QtCore import QTimer, QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys, time, os, json, setproctitle, subprocess, io
from style.Main_UI_ui import Ui_MainWindow
from functools import lru_cache


class Console(io.StringIO):
        def write(self, data: str):
            if data.strip():  # Only write non-empty lines
                sys.__stdout__.write(data)  # Write to the original stdout
                super().write(data)

@lru_cache
class Worker(QThread):
    finished = Signal(str)
    message_box_signal = Signal(str)
    progress_updated = Signal(int)
    

    def __init__(self, script_path):
        super().__init__()
        self.script_path = script_path
        self.main_window = Main_UI()
        self.p = None
        self.console_output = Console()
    
    def run(self):
        try:
            print(f'Trying to run process: {self.script_path}')
            setproctitle.setproctitle(f"MyApp: {self.script_path}")
            
            sys.stdout = self.console_output
            captured_output = self.console_output.getvalue()
            
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
                process = subprocess.Popen([r"venv\Scripts\python.exe",
                                self.script_path],
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
class Main_UI(QMainWindow):
    
    def __init__(self):
        # super(Main_UI, self).__init__()
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.test = self.ui.pushButton_12
        
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
            
    def display_message_box(self, message: str, icon=QMessageBox.Icon.Information):
        QMessageBox.information(self, 'Information', message, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton)
    
    def update_progress_bar(self, percent):
        self.progress_bar.setValue(percent)


def Main():
    app = QApplication(sys.argv)
    mainWindow = Main_UI()
    mainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    Main()