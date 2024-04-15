import asyncio, gc, pytest
from playwright.async_api import Playwright, async_playwright, expect


#importando Metodos principais
from Metodos import getPlanilha, checkup_login, getFromAPI, getBQ


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    total_lines_plan1 = getPlanilha.total_lines
    
    await checkup_login.checkup_login(page=page)
    
    cookies = await page.context.cookies(urls=baseURL)
    
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
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            
            await new_context.close()
            await new_browser.close()
            
            gc.collect()
            
            
async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())