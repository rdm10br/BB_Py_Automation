from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.Login import login
# from . import login
    
async def checkup_login(page: Page) -> None:
    baseURL = "https://sereduc.blackboard.com/"
    loginURL = f'{baseURL}webapps/login/'
        
    await page.goto(loginURL)
    await page.wait_for_load_state('networkidle')
    
    for attempt in range(3):
        try:
            if "Disciplinas" in await page.title():
                break
            else:
                attempt += 1
                await login.login(page=page)
                await page.wait_for_load_state('load')
        except Exception as e:
            if "Blackboard Learn" in await page.title():
                print(f"Error during login attempt: {attempt}")
                print(repr(e))