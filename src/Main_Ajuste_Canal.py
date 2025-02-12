import asyncio
from playwright.async_api import Page


from Metodos import getPlanilha, getFromAPI, ajuste_Canal, ajuste_manual
from Decorators.Main_StartUp import playwright_StartUp_nosub


@playwright_StartUp_nosub()
async def run(page: Page, index) -> None:
    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    
    classURL = f'./ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'
    
    print(id_externo)
    
    await page.goto(classUrlUltra)
    await ajuste_Canal.ajusteCanal(page=page, id_interno=id_interno, link='https://sereduc.blackboard.com/bbcswebdav/xid-522872899_1')
    await ajuste_manual.ajusteManual(page=page, id_interno=id_interno, link='https://sereduc.blackboard.com/bbcswebdav/xid-522872900_1')
    
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')

async def main():
    await run()

asyncio.run(main())