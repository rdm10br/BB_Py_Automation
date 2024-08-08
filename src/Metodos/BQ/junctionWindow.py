from PySide6.QtWidgets import (QApplication, QMainWindow,
    QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout)
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QTimer
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Escolha o BQ")
        self.setWindowOpacity(0.95)
        self.setWindowIcon(QIcon(r'src\Metodos\BQ\icons\folder.png'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setStyleSheet('background-color: #001A33;')
        
        self.window_width = 300
        self.window_height = 150
        self.resize(self.window_width, self.window_height)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        
        self.label = QLabel("É uma junção?", self)
        self.label.setStyleSheet('color: white;')
        layout.addWidget(self.label)

        button_layout = QHBoxLayout()
        
        self.yes_button = QPushButton("Sim", self)
        self.yes_button.setStyleSheet('background-color: #393D5C; color: white;')
        button_layout.addWidget(self.yes_button)
        
        self.no_button = QPushButton("Não", self)
        self.no_button.setStyleSheet('background-color: #393D5C; color: white;')
        button_layout.addWidget(self.no_button)
        
        layout.addLayout(button_layout)
        
        self.yes_button.clicked.connect(self.choose_yes)
        self.no_button.clicked.connect(self.choose_no)

        QTimer.singleShot(0, self.center_window)
    
    def center_window(self):
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        if screen:
            screen_geometry = screen.geometry()
            window_geometry = self.frameGeometry()
            x = screen_geometry.x() + (screen_geometry.width() - window_geometry.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - window_geometry.height()) // 2
            self.move(x, y)
    
    def choose_yes(self):
        self.choice = 'Yes'
        self.setDisabled(True)
        self.close()
        
    def choose_no(self):
        self.choice = 'No'
        self.setDisabled(True)
        self.close()

def window():
    print('Waiting for user choice...')
    app = QApplication.instance()  # Check if QApplication already exists
    if app is None:  # If not, create one
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    return window.choice if hasattr(window, 'choice') else None

if __name__ == "__main__":
    user_choice = window()
    if user_choice:
        print(f'User chose: {user_choice}')
    else:
        print('No choice was made')