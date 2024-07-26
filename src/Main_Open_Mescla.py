import asyncio
from playwright.async_api import Page, expect

from Metodos import getPlanilha, getFromAPI, openMescla
from Decorators.Main_StartUp import playwright_StartUp_nosub


@playwright_StartUp_nosub
async def run(page: Page, index) -> None:
    
        id_externo = getPlanilha.getCell(index=index)
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        await openMescla.open_Mescla(page=page, id_interno=id_interno)
        
        print(id_externo)
        
        

async def main():
    await run()

asyncio.run(main())