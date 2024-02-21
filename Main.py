from playwright.sync_api import Playwright, sync_playwright, expect

#importando Garbage Collector
import gc

#importando Metodos principais
from Metodos.Login import checkup_login
from Metodos.API import getFromAPI,getPlanilha

def run(playwright: Playwright) -> None:
    # Connect to the existing browser
    # adicionar ' --remote-debugging-port=9222' no final do destino do atalho do Chrome
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
    
        print(id_externo)
        new_page.goto(classUrlUltra)
        new_page.wait_for_load_state('networkidle')

        # // espaço onde você insere suas funções para executar no Loop //
        
        # // para criação de novos métodos utilizar o comando 'python -m playwright codegen' dentro do console para auxiliar na criação//
        
        context.new_page()
        
    context.close()

# Force garbage collection
gc.collect()

with sync_playwright() as playwright:
    run(playwright)