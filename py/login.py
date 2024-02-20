from playwright.sync_api import Playwright, sync_playwright, expect
import tkinter as tk
from tkinter import simpledialog

def get_credentials():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    # Ask for the username
    username = simpledialog.askstring("Input", "Digite seu Usuario:")
    # Ask for the password (masked)
    password = simpledialog.askstring("Input", "Digite sua senha:", show='*')

    return username, password

def login(playwright: Playwright) -> None:
        browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0]
        
        baseURL = "https://sereduc.blackboard.com/"
        loginURL = f'{baseURL}webapps/login/'
        ultraURL = f'{baseURL}ultra/course'
        
        page.goto(loginURL)
        page.wait_for_load_state('domcontentloaded')
        
        # page.get_by_role("button", name="OK").click()
        
        username, password = get_credentials()
        
        page.get_by_label("Nome de usuário").fill(username)
        page.get_by_label("Senha").fill(password)
        page.locator('#entry-login').click()
        page.goto(ultraURL)
        
# Testar a função
with sync_playwright() as playwright:
    login(playwright)