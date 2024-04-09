from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.Login import login
# from . import login

def wait_for_page_to_load(page):
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_load_state("load")
    page.wait_for_load_state("networkidle")
    
async def checkup_login(page: Page) -> None:
    
    for attempt in range(3):
        try:
            if "Disciplinas" in page.title():
                break
            else:
                attempt += 1
                await login.login(page=page)
                wait_for_page_to_load(page)
        except Exception as e:
            if "Blackboard Learn" in page.title():
                print(f"Error during login attempt: {attempt}")
                print(repr(e))