# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget
# import sys


# def window_file():
    
#     def choose_file():
#         filename, _ = QFileDialog.getOpenFileName(None, "Choose File", "", "All Files (*)")
#         if filename:
#             app.quit()  # Close the application if a file is selected
#         return filename

#     # Create the main application instance
#     app = QApplication(sys.argv)

#     # Create a main window
#     window = QMainWindow()
#     window.setWindowTitle("File Chooser")
    
#     # Create a button to trigger file selection
#     choose_button = QPushButton("Choose File", window)
#     choose_button.setGeometry(50, 50, 150, 50)

#     # Connect button click to choose_file() function
#     choose_button.clicked.connect(lambda: print('the path is: ', choose_file()))
#     # choose_button.clicked.connect(lambda: choose_file())

#     # Show the main window
#     window.show()

#     # Start the event loop
#     sys.exit(app.exec())
    
# window_file()


from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
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

    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Escolha o arquivo", "", "All Files (*)")
        if filename:
            QMainWindow.close(self)
            


def window_file():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window_file()