from playwright.sync_api import Playwright, sync_playwright, expect
import login

def wait_for_page_to_load(page):
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_load_state("load")
    page.wait_for_load_state("networkidle")
    
def checkup_login(playwright: Playwright) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    baseURL = "https://sereduc.blackboard.com/"
    
    for attempt in range(3):
        try:
            if "Disciplinas" in page.title():
                break
            else:
                attempt += 1
                login.login(playwright)
                wait_for_page_to_load(page)
        except Exception as e:
            if "Blackboard Learn" in page.title():
                print(f"Error during login attempt: {attempt}")
                
# Function test
with sync_playwright() as playwright:
    checkup_login(playwright)