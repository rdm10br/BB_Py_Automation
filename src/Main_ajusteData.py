import asyncio
from playwright.async_api import Page, expect


from Metodos import getPlanilha, getFromAPI, getData, ajusteData
from Decorators.Main_StartUp import playwright_StartUp


dataShow, dataHide = getData.get_data()


@playwright_StartUp
async def run(page: Page, index) -> None:

    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)

    
    classURL = f'./ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'
    classBulkEdit = f'{classUrlUltra}/bulkEditContent'

    print(id_externo)

    await page.goto(classBulkEdit)

    await ajusteData.ajusteData(page=Page, dataShow=dataShow, dataHide=dataHide)
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()


asyncio.run(main())