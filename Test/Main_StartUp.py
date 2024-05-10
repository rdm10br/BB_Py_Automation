import asyncio, gc, pytest, os, sys, time
from functools import wraps
from playwright.async_api import Playwright, async_playwright, Page

# from modulefinder import ModuleFinder
# finder = ModuleFinder()
# finder.find_module(name='Metodos', path='..')

from Metodos import (getPlanilha, checkup_login, getFromAPI,
                    capture_console_output_async, TimeStampedStream)


def playwright_StartUp(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with async_playwright() as playwright:
            
            sys.stdout = TimeStampedStream(sys.stdout)
            
            browser = await playwright.chromium.launch(headless=False)
            context = await browser.new_context(no_viewport=True)
            page = await context.new_page()
            
            await checkup_login.checkup_login(page=page)
            
            cookies = await page.context.cookies(urls="https://sereduc.blackboard.com/")
            
            total_lines_plan1 = getPlanilha.total_lines
            
            for index in range(total_lines_plan1):
                index+=1
                
                cell_status = getPlanilha.getCell_status(index=index)
                start_time = time.time()
                
                if cell_status == 'nan':
                    new_context = await browser.new_context(no_viewport=True)
                    await new_context.add_cookies(cookies)
                    new_page = await new_context.new_page()
                    
                    await func(new_page, index, *args, **kwargs)
                    
                    await new_page.close()
                    await new_context.close()
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    executionTime = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                    print('{:5} | {}'.format(f'Run: {index}',executionTime))
                    
                    gc.collect()
                    
            await browser.close()

    return wrapper

@playwright_StartUp
async def run(page: Page, index) -> None:
    
        id_externo = getPlanilha.getCell(index=index)
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        classUrlUltra = f'https://sereduc.blackboard.com/ultra/courses/{id_interno}/outline'
        
        print(id_externo)
        
        page.goto(classUrlUltra)

async def main():
    await run()

asyncio.run(main())