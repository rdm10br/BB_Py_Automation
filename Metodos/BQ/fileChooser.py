from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Escolha o BQ")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Escolha o arquivo do BQ:", self)
        layout.addWidget(self.label)

        self.choose_button = QPushButton("Escolha o arquivo", self)
        layout.addWidget(self.choose_button)

        self.choose_button.clicked.connect(self.choose_file)
        # self.setWindowIcon(QIcon.Mode.Disabled)

    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Escolha o arquivo", "", "All Files (*)")
        if filename:
            # print(filename)
            self.close()
            


def window_file():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window_file()