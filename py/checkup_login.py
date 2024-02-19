from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
import login

def wait_for_page_to_load(page):
    # Wait for the 'load' state, indicating that the entire page has loaded
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_load_state("load")

    # Additionally, you can wait for specific elements or conditions to ensure everything is ready
    page.wait_for_selector("body")  # Wait for the body element to be present

    # You can also wait for network activity to settle, indicating that all resources have been loaded
    page.wait_for_load_state("networkidle")
    
def checkup_login(playwright: Playwright) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    ultraURL = f'{baseURL}ultra/course'
    
    for attempt in range(3):
        try:
            if "Disciplinas" in page.title():
                break
            else:
                attempt += 1
                login.login(playwright)
                page.goto(ultraURL)
                wait_for_page_to_load(page)
        except Exception as e:
            if "Blackboard Learn" in page.title():
                print(f"Error during login attempt: {attempt}")