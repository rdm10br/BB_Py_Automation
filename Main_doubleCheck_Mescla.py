import asyncio, gc
from playwright.async_api import Playwright, async_playwright, expect


from Metodos import checkup_login, getFromAPI, getPlanilha, atribGrup, AjusteNotaZero, AjusteAvaliaçãoV2


async def run(playwright: Playwright) -> None:
    # Connect to the existing browser
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    
    # Access page
    await page.goto(baseURL)
    
    # Verificar se está logado e logar
    await checkup_login.checkup_login(page=page)
    
    cookies = await page.context.cookies(urls=baseURL)
    
    index = 0
    total_lines_plan1 = getPlanilha.total_lines
    
    context.new_page()
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_browser = await playwright.chromium.launch(headless=False)
            new_context = await new_browser.new_context(no_viewport=True) 
            # Assuming 'cookies' is the list of cookies obtained earlier
            await new_context.add_cookies(cookies)
            new_page = await new_context.new_page()
            
            #request from API
            id_externo = await getPlanilha.getCell(index=index)
            id_interno = await getFromAPI.API_Req(page=new_page, index=index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
            
            print(id_externo)
            await new_page.goto(classUrlUltra)
            
            # VETERANOS
            # atribGrup.inserirArquivoVET(page=new_page, id_interno)
            # atribGrup.atribuirGruposVET(page=new_page, id_interno)
            #===================
            
            # DIGITAL
            await atribGrup.inserirArquivoDIG(page=new_page, id_interno=id_interno)
            await atribGrup.atribuirGruposDIG(page=new_page, id_interno=id_interno)
            #===================
            
            await AjusteNotaZero.AjusteNotaZero(page=new_page, id_interno=id_interno)
            await AjusteAvaliaçãoV2.ajusteAvaliacao(page=new_page)
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            
            await new_context.close() 
            await new_browser.close() 
        
            gc.collect()
        

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())