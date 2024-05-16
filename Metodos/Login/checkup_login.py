from playwright.async_api import expect, Page

from Metodos.Login import login
# from . import login
    
async def checkup_login(page: Page) -> None:
    """
    Function that verify if you're loged in or not, and tries (3 times attempt) to login if
    you're not loged in

    Args:
        page (Page): Page constructor form Playwright that
        you want this function to run
    """
    baseURL = "https://sereduc.blackboard.com/"
    loginURL = f'{baseURL}webapps/login/'
    
    await page.goto(loginURL)
    await page.wait_for_load_state('networkidle')
    
    for attempt in range(3):
        try:
            if "Disciplinas" in await page.title():
                print('Logged in successfully!')
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