import asyncio, gc, sys
from playwright.async_api import Playwright, async_playwright, expect


from Metodos import (checkup_login, getFromAPI, getPlanilha, atribGrup,
AjusteNotaZero, AjusteAvaliaçãoV2, TimeStampedStream,
capture_console_output_async)

# @capture_console_output_async
async def run(playwright: Playwright) -> None:
    sys.stdout = TimeStampedStream(sys.stdout)
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    
    # Verificar se está logado e logar
    await checkup_login.checkup_login(page=page)
    
    cookies = await page.context.cookies(urls=baseURL)
    
    index = 0
    total_lines_plan1 = getPlanilha.total_lines
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_browser = await playwright.chromium.launch(headless=False)
            new_context = await new_browser.new_context(no_viewport=True)
            await new_context.add_cookies(cookies)
            new_page = await new_context.new_page()
            
            #request from API
            id_externo = getPlanilha.getCell(index=index)
            id_interno = await getFromAPI.API_Req(page=new_page, index=index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
            
            print(id_externo)
            await new_page.goto(classUrlUltra, wait_until='domcontentloaded')
            
            # VETERANOS
            await atribGrup.inserirArquivoVET(page=new_page, id_interno=id_interno)
            await atribGrup.atribuirGruposVET(page=new_page, id_interno=id_interno)
            #===================
            
            # DIGITAL
            # await atribGrup.inserirArquivoDIG(page=new_page, id_interno=id_interno)
            # await atribGrup.atribuirGruposDIG(page=new_page, id_interno=id_interno)
            #===================
            
            await AjusteNotaZero.AjusteNotaZero(page=new_page, id_interno=id_interno)
            await AjusteAvaliaçãoV2.ajusteAvaliacao(page=new_page, id_interno=id_interno)
            # getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            
            await new_context.close()
            await new_browser.close()
        
            gc.collect()
        

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())