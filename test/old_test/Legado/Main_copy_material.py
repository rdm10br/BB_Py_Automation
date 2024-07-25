from playwright.sync_api import Playwright, sync_playwright, expect

from Metodos import checkup_login, getPlanilha, copiaMaterial

def run(playwright: Playwright) -> None:
    # Connect to the existing browser
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    baseURL = "https://sereduc.blackboard.com/"
    # Access page
    page = context.pages[0]
    
    page.goto(baseURL)
    # Verificar se está logado e logar
    checkup_login.checkup_login(playwright = playwright)
    index = 0
    totalplan2 = getPlanilha.total_lines_plan2
    context.new_page()
    
    for index in range(totalplan2) :
        index +=1
        
        cell_status = getPlanilha.getCell_plan2_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_page = context.pages[1]
            page = context.pages[0]
            
            page.close()
            
            copiaMaterial.copyMaterial(playwright=playwright, index=index)
            getPlanilha.writeOnExcel_Plan2(index=index, return_status='OK')
            
            context.new_page()
        
    context.close()
    
with sync_playwright() as playwright:
    run(playwright)