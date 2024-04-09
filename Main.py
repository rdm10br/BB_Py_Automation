import asyncio
from playwright.async_api import Playwright, async_playwright, expect         #COLOCAR TUDO NAS OUTRAS
import pytest

#importando Garbage Collector
import gc      # COLOCAR TUDO NAS OUTRAS

#importando Metodos principais
from Metodos import getPlanilha, checkup_login, getFromAPI


async def run(playwright: Playwright) -> None:  #COLOCAR NAS OUTRAS
    browser = await playwright.chromium.launch(headless=False)  # COLOCAR NAS OUTRAS
    context = await browser.new_context(no_viewport=True)   # COLOCAR NAS OUTRAS
    page = await context.new_page()  # COLOCAR NAS OUTRAS
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    total_lines_plan1 = getPlanilha.total_lines
    
    # Access page
    await page.goto(baseURL)   # COLOCAR NAS OUTRAS
    
    # Verificar se está logado e logar
    await checkup_login.checkup_login(playwright=playwright)   # COLOCAR NAS OUTRAS
    
    # Salvar os cookies da página original
    cookies = await page.context.cookies(urls=baseURL)       # COLOCAR NAS OUTRAS
    
    
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_browser = await playwright.chromium.launch(headless=False)  # COLOCAR NAS OUTRAS
            new_context = await new_browser.new_context(no_viewport=True)   # COLOCAR NAS OUTRAS
            # Assuming 'cookies' is the list of cookies obtained earlier
            await new_context.add_cookies(cookies)  # COLOCAR NAS OUTRAS
            new_page = await new_context.new_page()  # COLOCAR NAS OUTRAS
            #request from API
            id_externo = await getPlanilha.getCell(index=index)   # COLOCAR NAS OUTRAS
            id_interno = await getFromAPI.API_Req(playwright=playwright, index=index)   # COLOCAR NAS OUTRAS
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
            
            print(id_externo)
            
            await new_page.goto(classUrlUltra)  # COLOCAR NAS OUTRAS

            # // espaço onde você insere suas funções para executar no Loop //
            
            # // para criação de novos métodos utilizar o comando 'python -m playwright codegen' 
            # dentro do console para auxiliar na criação//
            
            # // Lembre-se de sempre que criar um método novo adicionar a importação dele ao 
            # '__init__.py' do diretório de Metodos para facilitar sua importação//
            
            # Função para escrever na primeira planilha
            await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')   # COLOCAR NAS OUTRAS
            
            await new_context.close()   # COLOCAR NAS OUTRAS
            await new_browser.close()    # COLOCAR NAS OUTRAS
            
            # Force garbage collection
            await gc.collect()   # COLOCAR NAS OUTRAS

async def main():  # COLOCAR NAS OUTRAS
    async with async_playwright() as playwright: # COLOCAR NAS OUTRAS
        await run(playwright)  # COLOCAR NAS OUTRAS
asyncio.run(main())  # COLOCAR NAS OUTRAS