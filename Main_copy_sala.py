import asyncio
from playwright.async_api import Playwright, async_playwright, expect
from Metodos import checkup_login, getPlanilha, copiaSala

import gc

async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)  # COLOCAR NAS OUTRAS
    context = await browser.new_context(no_viewport=True)   # COLOCAR NAS OUTRAS
    page = await context.new_page()  # COLOCAR NAS OUTRAS

    baseURL = "https://sereduc.blackboard.com/"
    
    await page.goto(baseURL)
    
    # Verificar se está logado e logar
    await checkup_login.checkup_login(playwright=playwright)
    index = 0
    totalplan2 = getPlanilha.total_lines_plan2
    
    cookies = await page.context.cookies(urls=baseURL)
    
    for index in range(totalplan2) :
        index +=1
        
        cell_status = getPlanilha.getCell_plan2_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_browser = await playwright.chromium.launch(headless=False)  # COLOCAR NAS OUTRAS
            new_context = await new_browser.new_context(no_viewport=True)   # COLOCAR NAS OUTRAS
            # Assuming 'cookies' is the list of cookies obtained earlier
            await new_context.add_cookies(cookies)  # COLOCAR NAS OUTRAS
            new_page = await new_context.new_page()  # COLOCAR NAS OUTRAS
            
            await copiaSala.copySala(playwright=playwright, index=index)
            await getPlanilha.writeOnExcel_Plan2(index=index, return_status='CRIADA')
            
            await new_context.close()   # COLOCAR NAS OUTRAS
            await new_browser.close()
            
            await gc.collect()
        
    
async def main():  # COLOCAR NAS OUTRAS
    async with async_playwright() as playwright: # COLOCAR NAS OUTRAS
        await run(playwright)  # COLOCAR NAS OUTRAS
asyncio.run(main())  # COLOCAR NAS OUTRAS