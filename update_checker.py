import requests, zipfile, os, json


def check_for_updates(current_version):
    # response = requests.get('https://api.github.com/repos/rdm10br/BB_Py_Automation/releases/latest')
    response = requests.get('https://api.github.com/repos/rdm10br/BB_Py_Automation/releases/tags/pre-release')
    response.raise_for_status()
    latest_version = response.json().get('tag_name').lstrip('v')
    return latest_version if latest_version > current_version else None


def download_update(version):
    # url = f'https://github.com/rdm10br/BB_Py_Automation/archive/refs/tags/v{version}.zip'
    url = f'https://github.com/rdm10br/BB_Py_Automation/archive/refs/tags/{version}.zip'
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open('update.zip', 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def apply_update():
    with zipfile.ZipFile('update.zip', 'r') as zip_ref:
        zip_ref.extractall('update_directory')
    
    for filename in os.listdir('update_directory'):
        file_path = os.path.join('update_directory', filename)
        if os.path.isfile(file_path):
            os.replace(file_path, os.path.join('src', filename))  # Adjust path if needed


def restart_application():
    # Restart the application or prompt user to restart manually
    print("Please restart the application to apply the update.")


def main():
    CACHE_FILE = r'release.json'
    
    with open(CACHE_FILE, 'r', encoding="utf-8") as f:
        cache_data = json.load(f)
        
    CURRENT_VERSION = cache_data['CURRENT_VERSION']
    latest_version = check_for_updates(CURRENT_VERSION)
    
    if latest_version:
        print(f'New version {latest_version} available. Updating...')
        download_update(latest_version)
        apply_update()
        restart_application()
        print('Update complete.')
    else:
        print('No updates available.')

if __name__ == "__main__":
    main()
