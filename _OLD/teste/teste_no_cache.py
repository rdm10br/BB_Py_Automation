import asyncio
from playwright.async_api import Playwright, async_playwright, expect

from Metodos.API import getPlanilha
from Metodos.Login import getCredentials

async def run (playwright: Playwright) :
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    
    baseURL = "https://sereduc.blackboard.com/"
    ultraURL = f'{baseURL}ultra/courses/'
    total_lines_plan1 = getPlanilha.total_lines
    
    await page.goto(baseURL)
     
    # await checkup_login.checkup_login(playwright=playwright)
    for attempt in range(3):
        try:
            if "Disciplinas" in await page.title():
                break
            else:
                attempt += 1
                loginURL = f'{baseURL}webapps/login/'
                
                await page.goto(loginURL)
                # await page.wait_for_load_state('networkidle')
                
                await page.get_by_role("button", name="OK").click()
                
                username, password = getCredentials.get_credentials()
                        
                await page.get_by_label("Nome de usuário").fill(value=username)
                await page.get_by_label("Senha").fill(value=password)
                await page.locator('#entry-login').click()
                await page.goto(ultraURL)
        except Exception as e:
            if "Blackboard Learn" in await page.title():
                await print(f"Error during login attempt: {attempt}")
                await print(repr(e))
    
    cookies = await page.context.cookies(urls=baseURL)
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            browser2 = await playwright.chromium.launch(headless=False)
            context2 = await browser2.new_context(no_viewport=True)
            await context2.add_cookies(cookies)
            page2 = await context2.new_page()
            page3 = await context2.new_page()
            
            #request from API
            id_externo = getPlanilha.getCell(index=index)
            # id_interno = getFromAPI.API_Req(playwright=playwright, index=index)
            internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'
            
            await page3.goto(internalID_API)
            id_interno = await page3.evaluate('() => {return JSON.parse(document.body.innerText).id}')
            await page3.close()
            str(id_interno)
            
            classUrlUltra = f'{ultraURL}{id_interno}/outline'
            
            print(id_externo)
            
            await page2.goto(classUrlUltra)
            
            await context2.close()
            await browser2.close()
    

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())