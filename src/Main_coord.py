import asyncio
from playwright.async_api import Page

from Metodos import getFromAPI, getPlanilha, Prof
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index: int) -> None:
        
        id_externo, user = getPlanilha.getCell(index=index).split(',')
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        print(f'Coordenador a ser liberado : {user} na sala {id_externo}')
        
        await Prof.coord(page=page, id_interno=id_interno, user=user)
        
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()


asyncio.run(main())