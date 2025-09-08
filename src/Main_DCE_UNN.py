import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI, DCE_Mescla, getPlanilha, openMescla
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index: int) -> None:
    
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        await DCE_Mescla.adjust_name(page=page, id_interno=id_interno, name='Dce Uninorte')
        # await openMescla.open_Mescla(page=page, id_interno=id_interno)
        await openMescla.close_Mescla(page=page, id_interno=id_interno)
        
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()


asyncio.run(main())