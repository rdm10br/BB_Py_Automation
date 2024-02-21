# [13:51] Matheus Felipe Rosa Ferreira
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pandas as pd

# arq_excel = 'MAPEAMENTOS.xlsx'
# df_map = pd.read_excel(arq_excel, sheet_name='Plan1')

#python -m playwright codegen

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sereduc.blackboard.com/")
    page.get_by_role("button", name="OK").click()
    page.get_by_text("Nome de usuário").click()
    page.get_by_label("Nome de usuário").fill("matheus.rosa")
    page.get_by_label("Senha").click()
    page.get_by_label("Senha").fill("matheus013191095")
    page.get_by_role("button", name="Fazer login").click()
    
with sync_playwright () as playwright:
    run(playwright)