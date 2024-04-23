from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog)
from PySide6.QtGui import QIcon
import sys, os

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Escolha o BQ")
        self.setWindowOpacity(0.95)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Escolha o arquivo do BQ:", self)
        layout.addWidget(self.label)

        self.choose_button = QPushButton("Escolha o arquivo", self)
        layout.addWidget(self.choose_button)
        
        self.choose_button.clicked.connect(self.choose_file)

    def choose_file(self) -> str:
        todosArquivos = 'All Files (*)'
        arquivosTexto = 'Text File (*.docx *.doc)'
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
            return self.fileName


def window_file():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    return window.fileName

if __name__ == "__main__":
    window_file()