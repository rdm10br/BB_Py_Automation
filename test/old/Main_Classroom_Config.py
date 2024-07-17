import asyncio
from playwright.async_api import Page, expect


from Metodos import getPlanilha, getFromAPI
from Decorators.Main_StartUp import playwright_StartUp


@playwright_StartUp
async def run(page: Page, index) -> None:

    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)

    baseURL = 'https://sereduc.blackboard.com/'
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    classUrlUltra = f'{classURL}/outline'
    
    print(id_externo)

    await page.goto(classUrlUltra)


async def main():
    await run()

asyncio.run(main())