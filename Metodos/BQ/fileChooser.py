from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtGui import QIcon
import sys, os

class MainWindow(QMainWindow):
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
        filename, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Escolha o arquivo",
            #apenas informando que a separação de cada opção de 
            # filtro é por ';;'
            filter=f"{todosArquivos};;{arquivosTexto}",
            selectedFilter=arquivosTexto
            )
        if filename:
            print(f'\n O arquivo selecionado tem o caminho: {filename}\n')
            self.setDisabled(True)
            # self.close()
            # self.destroy()


def window_file():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    # app.exec()

if __name__ == "__main__":
    window_file()