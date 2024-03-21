from playwright.sync_api import Playwright, sync_playwright, expect

from Metodos import checkup_login, getFromAPI, getPlanilha, atribGrup, AjusteNotaZero, AjusteAvaliaçãoV2


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
    checkup_login.checkup_login(playwright=playwright)
    
    index = 0
    total_lines_plan1 = getPlanilha.total_lines
    
    context.new_page()
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_page = context.pages[1]
            page = context.pages[0]
            
            page.close()
            
            #request from API
            id_externo = getPlanilha.getCell(index=index)
            id_interno = getFromAPI.API_Req(playwright=playwright, index=index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
            
            print(id_externo)
            new_page.goto(classUrlUltra)
            new_page.wait_for_load_state('networkidle')
            
            # VETERANOS
            # atribGrup.inserirArquivoVET(playwright, id_interno)
            # atribGrup.atribuirGruposVET(playwright, id_interno)
            #===================
            
            # DIGITAL
            atribGrup.inserirArquivoDIG(playwright=playwright, id_interno=id_interno)
            atribGrup.atribuirGruposDIG(playwright=playwright, id_interno=id_interno)
            #===================
            
            AjusteNotaZero.AjusteNotaZero(playwright=playwright, id_interno=id_interno)
            AjusteAvaliaçãoV2.ajusteAvaliacao(playwright=playwright)
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            
            # context.storage_state()
            # context.clear_cookies()
            
            context.new_page()
        
        
    context.close()
    
with sync_playwright() as playwright:
    run(playwright)