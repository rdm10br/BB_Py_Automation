# import sys
# from PySide6 import QtCore, QtWidgets, QtGui


# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
        
#         self.input = QtWidgets.QTextEdit(alignment=QtCore.Qt.AlignCenter, text='teste')
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.input,stretch=False)
        
        
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()

#     sys.exit(app.exec())

import sys
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit,
                             QLabel, QPushButton, QVBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon  # Optional: for window icon

class LoginWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")  # Set window title

        # Optional: Set window icon
        # self.setWindowIcon(QIcon("path/to/your/icon.png"))

        self.username_label = QLabel("Username:")
        self.username_edit = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit(echoMode=QLineEdit.EchoMode.Password)  # Hide password

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Implement your login logic here (e.g., check credentials against a database)
        if username == "correct_username" and password == "correct_password":
            # Login successful
            print("Login successful!")
            self.close()  # Close the login window (optional)
        else:
            # Login failed
            print("Invalid username or password.")
            # Optionally, display an error message to the user

# Create an instance of the LoginWindow and show it
if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
