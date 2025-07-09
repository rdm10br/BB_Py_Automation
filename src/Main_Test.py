import asyncio
from playwright.async_api import Page

from Metodos import getPlanilha, getFromAPI
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index) -> None:
    # print('Hello, world!')
    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    
    classURL = f'./ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'
    
    print(id_externo)
    
    await page.goto(classUrlUltra)
    await page.wait_for_timeout(1000*2)
    # await page.pause()

async def main():
    await run()

asyncio.run(main())