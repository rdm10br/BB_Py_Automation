import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI, getPlanilha
from Decorators.Main_StartUp import playwright_StartUp


@playwright_StartUp
async def run(page: Page, index) -> None:
    
    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    print(id_externo)
    
    await getFromAPI.API_AP_all_folders(page, id_interno)
    
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()


asyncio.run(main())