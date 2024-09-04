import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI, AjusteNotaZero
from Decorators.Main_StartUp import playwright_StartUp_nosub


@playwright_StartUp_nosub
async def run(page: Page, index) -> None:
    
        id_externo = 'SALA_ELCIO'
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        print(id_externo)
        
        await AjusteNotaZero.AjusteNotaZero(page=page, id_interno=id_interno)


async def main():
    await run()


asyncio.run(main())