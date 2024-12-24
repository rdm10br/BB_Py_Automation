from PySide6.QtWidgets import (QApplication, QMainWindow,
    QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog)
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QTimer
import sys, json, os

class MainWindow(QMainWindow):
    def __init__(self, bq_name: str) -> None:
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
        
        if bq_name != '':
            self.label = QLabel(f"Escolha a junção de {bq_name}:", self)
        else:
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
        
    def choose_file(self) -> list[str]:
        todosArquivos = 'All Files (*)'
        # arquivosTexto = 'Text File (*.docx *.doc)'
        arquivosTexto = 'Text File (*.docx)'
        self.fileName, _ = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Escolha o arquivo",
            #apenas informando que a separação de cada opção de
            # filtro é por ';;'
            filter=f"{todosArquivos};;{arquivosTexto}",
            selectedFilter=arquivosTexto
            )
        if self.fileName:
            # print(f'\n O arquivo selecionado tem o caminho: {self.fileName}\n')
             # Initialize an empty list for the selected files
            queue_files = []

            # Iterate over the selected files
            for file_path in self.fileName:
                file_info = {
                    "path": file_path,
                    "questionCount": 0,       # Default value
                    "questionsMade": 0,       # Default value
                    "processingStatus": "Not Started",  # Default value
                    # "isJunction": ""       # Default value
                }
                queue_files.append(file_info)
                
            # Define the path to the JSON file
            json_file_path = r"src\Metodos\BQ\__pycache__\queue_files.json"

            # Check if the file exists
            if os.path.exists(json_file_path):
                try:
                    # Load the existing data
                    with open(json_file_path, "r", encoding="utf-8") as json_file:
                        data = json.load(json_file)
                    
                    # Ensure the key exists and append new data
                    if "queue_files" in data:
                        data["queue_files"].extend(queue_files)
                    else:
                        data["queue_files"] = queue_files
                except json.JSONDecodeError:
                    # Handle corrupted or empty JSON file
                    data = {"queue_files": queue_files}
            else:
                # If the file does not exist, initialize new data
                data = {"queue_files": queue_files}

            # Write the updated or new data back to the file
            with open(json_file_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
                
            self.setDisabled(True)
            self.close()
            print(f'file choosen path: {self.fileName}')
            return self.fileName


def window_file(bq_name: str = ''):
    print('choosing file...')
    app = QApplication.instance()  # Check if QApplication already exists
    if app is None:  # If not, create one
        app = QApplication(sys.argv)
    window = MainWindow(bq_name)
    window.show()
    app.exec()
    return window.fileName

if __name__ == "__main__":
    window_file()