# import asyncio
# from playwright.async_api import Playwright, async_playwright, expect
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

#importando Garbage Collector
import gc

#importando Metodos principais
from Metodos.Login import checkup_login
from Metodos.API import getFromAPI,getPlanilha
# from Metodos.Master import AjusteSofiaV2,AjusteSermelhor,AjusteAvaliaçãoV2


def main(playwright: Playwright) -> None:
    # Connect to the existing browser
    # adicionar ' --remote-debugging-port=9222' no final do destino do atalho do Chrome
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    page = context.pages[0]
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    total_lines_plan1 = getPlanilha.total_lines
    
    # Access page
    page.goto(baseURL)
    
    # Verificar se está logado e logar
    checkup_login.checkup_login(playwright)
    
    # Salvar os cookies da página original
    cookies = page.context.cookies()
    
    # # Create a new context with the saved storage state.
    new_context = browser.new_context(no_viewport=True)
    # Assuming 'cookies' is the list of cookies obtained earlier
    new_context.add_cookies(cookies)
    new_page = new_context.new_page()
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index)
        
        if cell_status == 'OK':
            pass
        else :
            #request from API
            id_externo = getPlanilha.getCell(index)
            id_interno = getFromAPI.API_Req(playwright,index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
            
            print(id_externo)
            
            new_page.goto(classUrlUltra)
            new_page.wait_for_load_state('networkidle')

            # // espaço onde você insere suas funções para executar no Loop //
            
            # // para criação de novos métodos utilizar o comando 'python -m playwright codegen' dentro do console para auxiliar na criação//
            
            # Função para escrever na primeira planilha
            getPlanilha.writeOnExcel_Plan1(index, 'OK')
            
            # Atualizando a referência dos contextos
            old_context = new_context
            
            # Create a new context with cookies after login.
            new_context = browser.new_context(no_viewport=True)
            new_context.add_cookies(cookies)
            new_page = new_context.new_page()
            
            # Fecha o contexto anterior
            old_context.close()
            
            # Force garbage collection
            gc.collect()
        
    context.close()

with sync_playwright() as playwright:
    main(playwright)