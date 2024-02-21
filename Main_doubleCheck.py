from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
from Metodos import checkup_login
from Metodos import getFromAPI
from Metodos import getPlanilha
from Metodos import atribGrup
from Metodos import AjusteAvaliaçãoV2
from Metodos import AjusteNotaZero

def run(playwright: Playwright) -> None:
    # Connect to the existing browser
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    page = context.pages[0]
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    
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
        id_externo = getPlanilha.getCell(index)
        id_interno = getFromAPI.API_Req(playwright,index)
        
        classUrlUltra = f'{classURL}{id_interno}/outline'
        # context.clear_browser_cache()
        
        print(id_externo)
        new_page.goto(classUrlUltra)
        new_page.wait_for_load_state('networkidle')
        
        atribGrup.atribuirGruposVET(playwright, id_interno)
        atribGrup.inserirArquivoVET(playwright, id_interno)
        AjusteNotaZero.AjusteNotaZero(playwright, id_interno)
        AjusteAvaliaçãoV2.ajusteAvaliacao(playwright)
        getPlanilha.writeOnExcel_Plan1(index, 'OK')
        
        # context.storage_state()
        # context.clear_cookies()
        # Clear cache while preserving login credentials
        # context.clear_storage_state()
        
        context.new_page()
        
        
    context.close()
    
with sync_playwright() as playwright:
    run(playwright)