from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
# from memory_profiler import profile
# from line_profiler import LineProfiler
# import cProfile
import gc

import checkup_login
import getFromAPI
import getPlanilha
import AjusteSofiaV2
import AjusteAvaliaçãoV2
import AjusteSermelhor

# @profile
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
    
        print(id_externo)
        new_page.goto(classUrlUltra)
        
        new_page.wait_for_load_state('networkidle')
        AjusteSofiaV2.ajusteSofia(playwright,id_interno)
        
        AjusteAvaliaçãoV2.ajusteAvaliacao(playwright,id_interno)
        
        AjusteSermelhor.ajusteSerMelhor(playwright)
        
        getPlanilha.writeOnExcel_Plan1(index, 'OK')
        
        context.new_page()
        
    context.close()

# Force garbage collection
gc.collect()

with sync_playwright() as playwright:
    # lp = LineProfiler()
    # lp.add_function(run)
    # lp.run('run(playwright)')
    # lp.print_stats()
    # cProfile.run('run()')
    run(playwright)