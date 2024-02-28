from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
import gc

from Metodos.Login import checkup_login
from Metodos.API import getFromAPI ,getPlanilha
from Metodos.Mescla import gruposAtividades

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
        
        cell_status = getPlanilha.getCell_status(index)
        
        if cell_status != '':
            pass
        else :
            new_page = context.pages[1]
            page = context.pages[0]
            
            page.close()
            
            #request from API
            id_externo = getPlanilha.getCell(index)
            id_interno = getFromAPI.API_Req(playwright,index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
        
            print(id_externo)
            new_page.goto(classUrlUltra)
            
            gruposAtividades.inserirArquivoAV1(playwright ,id_interno)
            gruposAtividades.inserirArquivoAV2(playwright ,id_interno)
            gruposAtividades.atribuirGruposAV1(playwright ,id_interno)
            gruposAtividades.atribuirGruposAV2(playwright ,id_interno)
            
            context.new_page()
            
            # Force garbage collection
            gc.collect()
        
    context.close()

with sync_playwright() as playwright:
    run(playwright)