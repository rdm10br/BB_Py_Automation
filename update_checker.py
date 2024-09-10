import requests, zipfile, os, json, tempfile, shutil, logging, time, base64
from dotenv import load_dotenv
from updater_rollback import rollback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GIT_REPO = os.getenv('GIT_REPO')
BRANCH = os.getenv('BRANCH')


def check_for_updates(current_version: str):
    try:
        # response = requests.get(f'https://api.github.com/repos/{GIT_REPO}/releases/tags/pre-release')
        response = requests.get(f'https://api.github.com/repos/{GIT_REPO}/releases/latest')
        response.raise_for_status()
        latest_version: str = response.json().get('name').lstrip('v')
        
        latest_version_tuple = tuple(map(int, latest_version.split('.')))
        current_version_tuple = tuple(map(int, current_version.split('.')))
        
        return latest_version if latest_version_tuple > current_version_tuple else None
    except Exception as e:
        logging.error(f"Failed to check for updates: {e}")
        return None


def download_update(version):
    # url = 'https://github.com/{GIT_REPO}/archive/refs/tags/pre-release.zip'
    url = f'https://github.com/{GIT_REPO}/archive/refs/tags/v{version}.zip'
    retries=3
    delay=5
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open('update.zip', 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            logging.info("Update downloaded successfully.")
            return  # Exit the function if successful
        except Exception as e:
            logging.error(f"Failed to download update (Attempt {attempt + 1}/{retries}): {e}")
            attempt += 1
            if attempt < retries:
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logging.error("All download attempts failed.")


def download(item: str):
    url = f'https://api.github.com/repos/{GIT_REPO}/contents/{item}?ref={BRANCH}'
    retries=3
    delay=5
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open('update.zip', 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            logging.info("Update downloaded successfully.")
            return  # Exit the function if successful
        except Exception as e:
            logging.error(f"Failed to download {item} (Attempt {attempt + 1}/{retries}): {e}")
            attempt += 1
            if attempt < retries:
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logging.error("All download attempts failed.")


def compare_items_from_git(item: str) -> str:
    url = f'https://api.github.com/repos/{GIT_REPO}/contents/{item}?ref={BRANCH}'
    try:
        response = requests.get(url)
        content = response.json().get('content')
        response.raise_for_status()
        
        decoded_content = base64.b64decode(content).decode('utf-8')
        
        local_file_path = f'./{item}'
        with open(local_file_path, 'r', encoding='utf-8') as local_file:
            local_file_content = local_file.read()
            
        if decoded_content == local_file_content:
            logging.info("The contents are identical.")
            return None
        else:
            logging.info("The contents are different.")
            return str(response.json().get('download_url'))
    except Exception as e:
        logging.warning("Failed to retrieve the content from GitHub.")


def compare_items(item: str, tmpdirname: str) -> str:
    try:
        local_file_path = f'./{item}'
        with open(local_file_path, 'r', encoding='utf-8') as local_file:
            local_file_content = local_file.read()
        
        downloaded_content_path = f'{tmpdirname}/{item}'
        with open(downloaded_content_path, 'r', encoding='utf-8') as local_file:
            downloaded_content = local_file.read()
        
        if downloaded_content == local_file_content:
            logging.info("The contents are identical.")
            return None
        else:
            logging.info("The contents are different.")
            return ''
    except Exception as e:
        logging.warning("Failed to retrieve the content from GitHub.")


def apply_update():
    try:
        with tempfile.TemporaryDirectory() as tmpdirname:
            with zipfile.ZipFile('update.zip', 'r') as zip_ref:
                zip_ref.extractall(tmpdirname)
            
            top_level_dirs = next(os.walk(tmpdirname))[1]
            single_top_dir = top_level_dirs[0] if len(top_level_dirs) == 1 else None
            
            for root, dirs, files in os.walk(tmpdirname):
                for filename in files:
                    src_file_path = os.path.join(root, filename)
                    
                    # Determine the relative path within the extracted structure
                    relative_path = os.path.relpath(src_file_path, tmpdirname)
                    
                    relative_path = os.path.relpath(src_file_path, os.path.join(tmpdirname, single_top_dir))
                    
                    dest_file_path = os.path.join(os.getcwd(), relative_path)
                    
                    # Ensure the destination directory exists
                    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                    
                    logging.info(f'Updating {filename} to {dest_file_path}...')
                    
                    # Move the file to the destination path
                    shutil.move(src_file_path, dest_file_path)
        
        os.remove('update.zip')
        logging.info("Update applied successfully.")
    except Exception as e:
        logging.error(f"Failed to apply update: {e}")
        raise


def main():
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
    
    if latest_version:
        logging.info(f'New version: \'{latest_version}\' available, Current version: \'{CURRENT_VERSION}, Updating...')
        try:
            download_update(latest_version)
            apply_update()
            logging.info('Update complete.')
        except Exception as e:
            logging.error(f"Update failed: {e}")
            try:
                logging.warning('Rollback Needed...')
                logging.info('Rollbacking in 1 version...')
                version = rollback(1)
                download_update(version)
                apply_update()
            except:
                logging.error('Lost internet connection or Update Failed')

    else:
        logging.info('No updates available.')


if __name__ == "__main__":
    main()