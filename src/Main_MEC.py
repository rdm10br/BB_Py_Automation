import asyncio, os
from playwright.async_api import Page

from Metodos import getFromAPI, DCE_Mescla, remove_ser, getPlanilha
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index: int) -> None:
    
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        await DCE_Mescla.adjust_name(page=page, id_interno=id_interno, name='Master')
        
        item = ['Avaliações',
                'Fale com o Tutor',
                'Manuais',
                'SER Melhor (Clique Aqui para deixar seu elogio, crítica ou sugestão)']
        for i in item:
            await remove_ser.removeSer(page=page, id_interno=id_interno, item=i)
        
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()
    # os.system("shutdown /s /t 0")


asyncio.run(main())