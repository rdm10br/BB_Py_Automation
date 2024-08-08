import asyncio, gc,  sys, os
from playwright.async_api import Playwright, async_playwright, expect
from dotenv import load_dotenv

from Metodos import checkup_login, getPlanilha, copiaSala
from Decorators import capture_console_output_async, TimeStampedStream


@capture_console_output_async
async def run(playwright: Playwright) -> None:
    load_dotenv()
    baseURL = os.getenv('BASE_URL')
    
    sys.stdout = TimeStampedStream(sys.stdout)
    browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context = await browser.new_context(base_url=baseURL, no_viewport=True)
    page = await context.new_page()

    
    
    await page.goto('./')
    
    # Verificar se está logado e logar
    await checkup_login.checkup_login(page=page)
    
    index = 0
    totalplan2 = getPlanilha.total_lines_plan2
    
    cookies = await page.context.cookies(urls=baseURL)
    
    for index in range(totalplan2) :
        index +=1
        
        cell_status = getPlanilha.getCell_plan2_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'])
            new_context = await new_browser.new_context(base_url=baseURL, no_viewport=True)
            # Assuming 'cookies' is the list of cookies obtained earlier
            await new_context.add_cookies(cookies)
            new_page = await new_context.new_page()
            
            await copiaSala.copySala(page=new_page, index=index)
            getPlanilha.writeOnExcel_Plan2(index=index, return_status='CRIADA')
            
            await new_context.close()
            await new_browser.close()
            
            gc.collect()
        
    
async def main():
    async with async_playwright() as playwright: # COLOCAR NAS OUTRAS
        await run(playwright)
asyncio.run(main())