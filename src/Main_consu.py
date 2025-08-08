import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI, getPlanilha, consu
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index: int) -> None:
    
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        await consu.ajusteConsu(page=page, id_interno=id_interno)
        
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()


asyncio.run(main())