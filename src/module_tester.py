import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI
from Decorators.Main_StartUp import playwright_StartUp_nosub
from Decorators import Inscryption


@playwright_StartUp_nosub
async def run(page: Page, index) -> None:
    
        id_externo = 'SALA_ELCIO'
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        print(id_externo)
        
        # await AjusteNotaZero.AjusteNotaZero(page=page, id_interno=id_interno)
        # await getFromAPI.API_AP_all_folders(page, id_interno)
        # await Inscryption.Auto_Unsub(page, index)


async def main():
    await run()


asyncio.run(main())