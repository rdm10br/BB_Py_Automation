from PySide6.QtWidgets import (QApplication, QLabel, QVBoxLayout, QSpinBox,
                               QPushButton, QDialog)
from PySide6.QtGui import QIcon, QFontDatabase
import requests, os, json, logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GIT_REPO = os.getenv('GIT_REPO')
BRANCH = os.getenv('BRANCH')

class RegressWindow(QDialog):
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

def get_versions():
    app = QApplication([])  # Initialize the application
    window = RegressWindow()  # Create the dialog window
    
    if window.exec():  # This shows the window and waits for the user to submit
        return window.num_versions  # Return the selected number of versions


def rollback(regression: int):
    url = f'https://api.github.com/repos/{GIT_REPO}/tags'
    response = requests.get(url)
    response.raise_for_status()
    
    tags = response.json()
    if tags:
        if regression is None:
            logging.warning('Regression NoneType, deafult regression is 1')
            regression = 1
            
        if regression > len(tags):
            logging.warning('Regression out of index, deafult regression is 1')
            regression = 1
            logging.info(f'Regressing: `{regression}` version')
            tag: json = tags[regression]
            name: str = tag.get('name').lstrip('v')
            logging.info(f'Version: {name}')
            return name
        elif regression < len(tags):
            logging.info(f'Regressing: `{regression}` version')
            tag: json = tags[regression]
            name: str = tag.get('name').lstrip('v')
            logging.info(f'Version: {name}')
            return name
    else:
        print("No tags found or internet connection lost.")

def main():
    # Import Here to avoid circular import from update_checker
    from update_checker import download_update, check_for_updates, apply_update
    CACHE_FILE = r'release.json'
     
    try:
        with open(CACHE_FILE, 'r', encoding="utf-8") as f:
            cache_data = json.load(f)
    except FileNotFoundError:
        logging.warning(f"File {CACHE_FILE} not found. Creating with default version.")
        cache_data = {'CURRENT_VERSION': 'v0.0.0'}
        with open(CACHE_FILE, 'w', encoding='UTF-8') as file:
            json.dump(cache_data, file, ensure_ascii=False, indent=4)
    except json.JSONDecodeError:
        logging.warning(f"Error decoding {CACHE_FILE}. Resetting to default version.")
        cache_data = {'CURRENT_VERSION': 'v0.0.0'}
        with open(CACHE_FILE, 'w', encoding='UTF-8') as file:
            json.dump(cache_data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    CURRENT_VERSION = cache_data.get('CURRENT_VERSION').lstrip('v')
    if not CURRENT_VERSION:
        logging.error('Current version not found in cache. Resetting to default version.')
        cache_data = {'CURRENT_VERSION': 'v0.0.0'}
        with open(CACHE_FILE, 'w', encoding='UTF-8') as file:
            json.dump(cache_data, file, ensure_ascii=False, indent=4)
        return
    
    latest_version = check_for_updates(CURRENT_VERSION)
    
    if latest_version is None:
        logging.info('Available for RollBack.')
        regression = get_versions()
        # version = rollback(regression=regression)
        # download_update(version=version)
        # apply_update()
    else:
        logging.info(f'New version: \'{latest_version}\' available, Current version: \'{CURRENT_VERSION}, Updating...')
        try:
            download_update(latest_version)
            apply_update()
            logging.info('Update complete.')
        except Exception as e:
            logging.error(f"Update failed: {e}")

        
if __name__ == "__main__":
    main()