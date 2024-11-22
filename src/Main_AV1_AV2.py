#CODIGO PRA REMOVER O * DA AV1,AV2 E AF TORNANDO O ITEM VISIVEL E OCULTO NOVAMENTE

import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI, ajuste_av1_av2, getPlanilha
from Decorators.Main_StartUp import playwright_StartUp_nosub


@playwright_StartUp_nosub
async def run(page: Page, index) -> None:

        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        await ajuste_av1_av2.ajuste_mescla(page, id_interno)
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')

async def main():
    await run()


asyncio.run(main())