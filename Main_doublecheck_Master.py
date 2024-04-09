import asyncio
from playwright.async_api import Playwright, async_playwright, expect
# from memory_profiler import profile
# from line_profiler import LineProfiler
# import cProfile
import gc

from Metodos import checkup_login, getFromAPI, getPlanilha, AjusteSofiaV2, AjusteAvaliaçãoV2, AjusteSermelhor

# @profile
async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)  # COLOCAR NAS OUTRAS
    context = await browser.new_context(no_viewport=True)   # COLOCAR NAS OUTRAS
    page = await context.new_page()  # COLOCAR NAS OUTRAS
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    
    # Access page
    await page.goto(baseURL)
    
    # Verificar se está logado e logar
    await checkup_login.checkup_login(playwright=playwright)
    
    index = 0
    total_lines_plan1 = getPlanilha.total_lines
    
    cookies = await page.context.cookies(urls=baseURL)
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != "nan" :
            pass
        else :
            new_browser = await playwright.chromium.launch(headless=False)  # COLOCAR NAS OUTRAS
            new_context = await new_browser.new_context(no_viewport=True)   # COLOCAR NAS OUTRAS
            # Assuming 'cookies' is the list of cookies obtained earlier
            await new_context.add_cookies(cookies)  # COLOCAR NAS OUTRAS
            new_page = await new_context.new_page()  # COLOCAR NAS OUTRAS
            #request from API
            id_externo = await getPlanilha.getCell(index=index)
            id_interno = await getFromAPI.API_Req(playwright=playwright, index=index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
        
            print(id_externo)
            await new_page.goto(classUrlUltra)
            
            await AjusteSofiaV2.ajusteSofia(playwright=playwright, id_interno=id_interno)
            
            await AjusteAvaliaçãoV2.ajusteAvaliacao(playwright=playwright, id_interno=id_interno)
            
            await AjusteSermelhor.ajusteSerMelhor(playwright=playwright)
            
            await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            
            await new_context.close()   # COLOCAR NAS OUTRAS
            await new_browser.close()
            
            # Force garbage collection
            await gc.collect()
    

async def main():  # COLOCAR NAS OUTRAS
    async with async_playwright() as playwright: # COLOCAR NAS OUTRAS
        await run(playwright)  # COLOCAR NAS OUTRAS
asyncio.run(main())  # COLOCAR NAS OUTRAS