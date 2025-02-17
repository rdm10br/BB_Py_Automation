import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI, ajuste_position, DCE_Mescla
from Decorators.Main_StartUp import playwright_StartUp_nosub
from Decorators import Inscryption


@playwright_StartUp_nosub()
async def run(page: Page, index) -> None:
    
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        # await AjusteNotaZero.AjusteNotaZero(page=page, id_interno=id_interno)
        # await getFromAPI.API_AP_all_folders(page, id_interno)
        # await Inscryption.Auto_Unsub(page, index)
        # await ajuste_position.ajusteGradebook(page, id_interno)
        # await DCE_Mescla.adjust_name(page=page, id_interno=id_interno)


async def main():
    await run()


asyncio.run(main())