from PySide6.QtWidgets import (QApplication, QLabel, QVBoxLayout, QSpinBox,
                               QPushButton, QDialog)
from PySide6.QtGui import QIcon, QFontDatabase
import sys

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.load_stylesheet(r"src\style\style.qss")
        self.setWindowTitle("Select Regress Versions")
        self.setWindowIcon(QIcon(r'src\style\icon\automation0.png'))
        font_id = QFontDatabase.addApplicationFont(r"src\font\Poppins\Poppins-Regular.ttf")
        QFontDatabase.applicationFontFamilies(font_id)
        
        # Create layout and widgets
        layout = QVBoxLayout()
        
        self.label = QLabel("How many versions do you want to regress?")
        layout.addWidget(self.label)
        
        self.label2 = QLabel("[1 - 10]")
        layout.addWidget(self.label2)
        
        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(10)  # You can set it to any number you prefer
        layout.addWidget(self.spin_box)
        
        self.button = QPushButton("Submit")
        layout.addWidget(self.button)
        
        # Set the layout
        self.setLayout(layout)
        
        # Connect button click signal to slot
        self.button.clicked.connect(self.on_submit)
        
        # Store the number of versions selected
        self.num_versions = None
    
    def load_stylesheet(self, file_name):
        with open(file_name, "r") as file:
            self.setStyleSheet(file.read())
            
    def on_submit(self):
        # Capture the value from the spin box
        self.num_versions = self.spin_box.value()
        self.accept()  # Closes the dialog and returns control

def window():
    print('Waiting for user choice...')
    app = QApplication.instance()  # Check if QApplication already exists
    if app is None:  # If not, create one
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    return window.num_versions if hasattr(window, 'num_versions') else None

if __name__ == "__main__":
    user_choice = window()
    if user_choice:
        print(f'User chose: {user_choice}')
    else:
        print('No choice was made')