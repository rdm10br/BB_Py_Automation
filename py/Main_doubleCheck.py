from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
import checkup_login
import getFromAPI
import getPlanilha
import atribGrup
import AjusteAvaliação
import AjusteNotaZero

def run(playwright: Playwright) -> None:
    # Connect to the existing browser
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    page = context.pages[0]
    
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = baseURL+"ultra/courses/"
    
    # Access page
    page.goto(baseURL)
    # Verificar se está logado e logar
    checkup_login.checkup_login(playwright)
    index = 0
    total_lines_plan1 = getPlanilha.total_lines
    
    context.new_page()
    
    for index in range(total_lines_plan1) :
        index +=1
        new_page = context.pages[1]
        page = context.pages[0]
        
        page.close()
        #request from API
        id_interno = getFromAPI.API_Req(playwright,index)
        
        # context.clear_browser_cache()
    
        new_page.goto(classURL+id_interno+"/outline")
        new_page.wait_for_load_state('networkidle')
        
        atribGrup.atribuirGruposVET(playwright, id_interno)
        atribGrup.inserirArquivoVET(playwright, id_interno)
        AjusteNotaZero.AjusteNotaZero(playwright, id_interno)
        AjusteAvaliação.ajusteAvaliacao(playwright)
        getPlanilha.writeOnExcel_Plan1(index, 'OK')
        
        # context.clear_cookies()
        context.new_page()
        
        
    context.close()
    
with sync_playwright() as playwright:
    run(playwright)