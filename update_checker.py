import requests, zipfile, os, json, tempfile, shutil


def check_for_updates(current_version):
    # response = requests.get('https://api.github.com/repos/rdm10br/BB_Py_Automation/releases/tags/pre-release')
    response = requests.get('https://api.github.com/repos/rdm10br/BB_Py_Automation/releases/latest')
    response.raise_for_status()
    latest_version = response.json().get('name').lstrip('v')
    return latest_version if latest_version > current_version else None


def download_update(version):
    # url = 'https://github.com/rdm10br/BB_Py_Automation/archive/refs/tags/pre-release.zip'
    url = f'https://github.com/rdm10br/BB_Py_Automation/archive/refs/tags/v{version}.zip'
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open('update.zip', 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def apply_update():
    with tempfile.TemporaryDirectory() as tmpdirname:
        with zipfile.ZipFile('update.zip', 'r') as zip_ref:
            zip_ref.extractall(tmpdirname)
        
        # Determine if there is a single top-level directory in the extracted files
        top_level_dirs = next(os.walk(tmpdirname))[1]
        single_top_dir = top_level_dirs[0] if len(top_level_dirs) == 1 else None
        
        for root, dirs, files in os.walk(tmpdirname):
            for filename in files:
                src_file_path = os.path.join(root, filename)
                
                # Determine the relative path within the extracted structure
                relative_path = os.path.relpath(src_file_path, tmpdirname)
                
                # # If there's a single top-level directory, adjust the relative path
                # if single_top_dir:
                relative_path = os.path.relpath(src_file_path, os.path.join(tmpdirname, single_top_dir))
                
                dest_file_path = os.path.join(os.getcwd(), relative_path)
                
                # Ensure the destination directory exists
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                
                print(f'Updating {filename}...')
                print(f'Updating to {dest_file_path}...')
                # Move the file to the destination path
                shutil.move(src_file_path, dest_file_path)
    
    os.remove('update.zip')


def restart_application():
    print("Please restart the application to apply the update.")


def main():
    CACHE_FILE = r'release.json'
    
    try:
        with open(CACHE_FILE, 'r', encoding="utf-8") as f:
            cache_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nError reading the cache file.")
        return
    
    CURRENT_VERSION = cache_data.get('CURRENT_VERSION').lstrip('v')
    if not CURRENT_VERSION:
        print("\nCurrent version not found in cache.")
        return
    
    latest_version = check_for_updates(CURRENT_VERSION)
    
    if latest_version:
        print(f'\nNew version {latest_version} available. Updating...')
        download_update(latest_version)
        apply_update()
        # restart_application()
        print('\nUpdate complete.')
    else:
        print('\nNo updates available.')


if __name__ == "__main__":
    main()