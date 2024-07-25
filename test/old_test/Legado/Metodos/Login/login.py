from playwright.sync_api import Playwright, sync_playwright, expect

from Metodos.Login import getCredentials
# from . import getCredentials

def login(playwright: Playwright) -> None:
        browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0]
        
        baseURL = "https://sereduc.blackboard.com/"
        loginURL = f'{baseURL}webapps/login/'
        ultraURL = f'{baseURL}ultra/course'
        
        page.goto(loginURL)
        page.wait_for_load_state('networkidle')
        
        if page.locator('#agree_button').is_visible() :
                page.get_by_role("button", name="OK").click()
        else :
                pass
        
        username, password = getCredentials.get_credentials()
                
        page.get_by_label("Nome de usuário").fill(value=username)
        page.get_by_label("Senha").fill(value=password)
        page.locator('#entry-login').click()
        page.goto(ultraURL)
        
# Testar a função
# with sync_playwright() as playwright:
#     login(playwright)