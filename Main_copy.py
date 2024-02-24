from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *

from Metodos.Login import checkup_login
from Metodos.API import getPlanilha
from Metodos.Copia import copiaSala

def run(playwright: Playwright) -> None:
    # Connect to the existing browser
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    # Access page
    page = context.pages[0]

    baseURL = "https://sereduc.blackboard.com/"
    
    page.goto(baseURL)
    
    # Verificar se está logado e logar
    checkup_login.checkup_login(playwright)
    index = 0
    totalplan2 = getPlanilha.total_lines_plan2
    
    for index in range(totalplan2) :
        index +=1
        
        # Create a new context with the saved storage state.
        context1 = browser.new_context(storage_state=page.context.storage_state())
        page1 = context1.new_page()

        copiaSala.copySala(playwright,index)
        getPlanilha.writeOnExcel_Plan2(index,'CRIADA')
        
        context1.close()
        
    context.close()
    
with sync_playwright() as playwright:
    run(playwright)