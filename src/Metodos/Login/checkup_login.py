from datetime import datetime, timedelta
import json, os, time
from playwright.async_api import Page

from Metodos.Login import login
# from . import login

timer = time.strftime('%d-%m-%Y-%H-%M-%S')
CACHE_FILE = r'src\Metodos\Login\__pycache__\login_cache.json'
CACHE_DURATION_HOURS = 3


async def load_cookies_from_cache(page: Page) -> bool:
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            cache_data = json.load(f)
            cache_time = datetime.fromisoformat(cache_data['timestamp'])
            if datetime.now() - cache_time < timedelta(hours=CACHE_DURATION_HOURS):
                await page.context.add_cookies(cache_data['cookies'])
                return True
    return False


async def save_cookies_to_cache(page: Page) -> None:
    cookies = await page.context.cookies(urls='https://sereduc.blackboard.com/')
    cache_data = {
        'timestamp': datetime.now().isoformat(),
        'cookies': cookies
    }
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache_data, f)
        

async def checkup_login(page: Page) -> None:
    """
    Function that verify if you're loged in or not, and tries (3 times attempt) to login if
    you're not loged in

    Args:
        page (Page): Page constructor form Playwright that
        you want this function to run
    """
    # baseURL = "https://sereduc.blackboard.com/"
    loginURL = f'./webapps/login/'
    
    await page.goto(loginURL)
    await page.wait_for_load_state('domcontentloaded')
    
    if await load_cookies_from_cache(page):
        print('Using cache to login...')
        await page.goto('./')
        await page.wait_for_load_state('domcontentloaded')
        if "Disciplinas" in await page.title():
            print('Logged in successfully using cached cookies!')
            return
    else:
        for attempt in range(3):
            try:
                if "Disciplinas" in await page.title():
                    print('Logged in successfully!')
                    await save_cookies_to_cache(page)
                    break
                else:
                    attempt += 1
                    print(f'Trying to log in attempt: {attempt}')
                    await login.login(page=page)
                    await page.wait_for_load_state('networkidle')
                    await page.wait_for_load_state('domcontentloaded')
                    await page.wait_for_load_state('load')
            except Exception as e:
                if "Blackboard Learn" in await page.title():
                    print(f"Error during login attempt: {attempt}")
                    print(repr(e))