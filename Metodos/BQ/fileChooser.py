from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtGui import QIcon
# from PySide6.QtCore import pyqtSignal, SIGNAL
import sys, os

class MainWindow(QMainWindow):
    # my_signal = pyqtSignal(str)
    def __init__(self):
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

    def choose_file(self):
        todosArquivos = 'All Files (*)'
        arquivosTexto = 'Text File (*.docx *.doc)'
        fileName, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Escolha o arquivo",
            #apenas informando que a separação de cada opção de 
            # filtro é por ';;'
            filter=f"{todosArquivos};;{arquivosTexto}",
            selectedFilter=arquivosTexto
            )
        if fileName:
            print(f'\n O arquivo selecionado tem o caminho: {fileName}\n')
            # self.emit(fileName)
            self.setDisabled(True)
            self.close()
            # self.destroy()
            return fileName


def window_file():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window_file()