from PySide6.QtWidgets import (QApplication, QMainWindow,
    QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog)
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
        
        self.window_width = 250
        self.window_height = 100
        self.resize(self.window_width, self.window_height)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        
        self.label = QLabel("Escolha o arquivo do BQ:", self)
        self.label.setStyleSheet('color: white;')
        layout.addWidget(self.label)

        self.choose_button = QPushButton("Escolha o arquivo", self)
        self.choose_button.setStyleSheet('background-color: #393D5C; color: white;')
        layout.addWidget(self.choose_button)
        
        self.choose_button.clicked.connect(self.choose_file)

        QTimer.singleShot(0, self.center_window)
    
    def center_window(self):
        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)
        # screen_geometry = QApplication.primaryScreen().geometry()
        # window_geometry = self.frameGeometry()
        # x = (screen_geometry.width() - window_geometry.width()) // 2
        # y = (screen_geometry.height() - window_geometry.height()) // 2
        # self.move(x, y)
        if screen:
            screen_geometry = screen.geometry()
            window_geometry = self.frameGeometry()
            x = screen_geometry.x() + (screen_geometry.width() - window_geometry.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - window_geometry.height()) // 2
            self.move(x, y)
        
    def choose_file(self) -> str:
        todosArquivos = 'All Files (*)'
        # arquivosTexto = 'Text File (*.docx *.doc)'
        arquivosTexto = 'Text File (*.docx)'
        self.fileName, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Escolha o arquivo",
            #apenas informando que a separação de cada opção de
            # filtro é por ';;'
            filter=f"{todosArquivos};;{arquivosTexto}",
            selectedFilter=arquivosTexto
            )
        if self.fileName:
            print(f'\n O arquivo selecionado tem o caminho: {self.fileName}\n')
            self.setDisabled(True)
            self.close()
            print(f'file choosen path: {self.fileName}')
            return self.fileName


def window():
    print('choosing file...')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    return window.fileName

if __name__ == "__main__":
    window()