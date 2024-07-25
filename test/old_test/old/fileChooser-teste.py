import os
def open_file_dialog():
    file_path = browse_file()
    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected.")

def browse_file():
    file_path = None
    try:
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename()  # Open file dialog
    except ImportError:
        print("Tkinter is not available. Please provide the file path manually.")

    return file_path

open_file_dialog()