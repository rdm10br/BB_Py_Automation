import asyncio
from playwright.async_api import async_playwright, Page
import time

sheet_url = 'https://sereducacionalbr.sharepoint.com/:x:/r/sites/GraduaoEaD321'\
        '/Documentos%20Compartilhados/General/Enturma%C3%A7%C3%A3o%20-%2020242'\
        '/Montagem%20Masters%20e%20Mesclas%20-%2020242.xlsx?d='\
        'w3df95c8a92754b7da186df8c2c6e5c14&csf=1&web=1&e=yWhJ7S'

tenant_id = '5297d108-fab0-47d4-97f3-449e274ea38b'
oauth_link = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
file_id = ''
worksheet_name = ''
worksheet = f'https://graph.microsoft.com/v1.0/me/drive/items/{file_id}/workbook'\
            f'/worksheets/{worksheet_name}/range(address=\'A1:D10\')'
        
async def get_sheet_data(page: Page):
    # Acesse a planilha
    await page.goto(sheet_url)
    # Espere a página carregar
    await page.wait_for_selector('frame_locator("iframe[name=\"WacFrame_Excel_0\"]").locator("#Sheet0_0_0_1 canvas")"]')
    
    # Extraia os dados da planilha
    data = await page.evaluate('''
        () => {
            const rows = document.querySelectorAll('div[role="row"]');
            return Array.from(rows).map(row => {
                const cells = row.querySelectorAll('div[role="gridcell"]');
                return Array.from(cells).map(cell => cell.innerText);
            });
        }
    ''')
    return data

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0]
        
        # cookies = await page.context.cookies(urls="https://www.microsoft365.com/apps?auth=2&home=1")
        
        # context2 = await browser.new_context(no_viewport=True)
        # await context2.add_cookies(cookies)
        # page2 = await context.new_page()
        
        # await page.goto('https://www.microsoft365.com/apps?auth=2&home=1')
        await page.goto(sheet_url)
        await page.wait_for_timeout(5*10000)

        # Obtenha os dados iniciais da planilha
        old_data = await get_sheet_data(page)
        print("Dados iniciais:", old_data)

        while True:
            # Espere um intervalo de tempo antes de verificar novamente
            time.sleep(30)  # 30 segundos de intervalo
            
            # Obtenha os novos dados da planilha
            new_data = await get_sheet_data(page)
            print("Dados novos:", new_data)

            # Compare os dados
            if new_data != old_data:
                print("A planilha foi modificada!")
                # Adicione aqui o código para lidar com a mudança
                # Por exemplo, enviar uma notificação ou atualizar um banco de dados
                old_data = new_data
            else:
                print("Nenhuma modificação detectada.")

asyncio.run(main())