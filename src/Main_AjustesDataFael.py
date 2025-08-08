import asyncio
from playwright.async_api import Page


from Metodos import getPlanilha, getFromAPI, AjusteDataFael
from Decorators import playwright_StartUp


# dataShow, dataHide = getData.get_data()

@playwright_StartUp(autoSub=True)
async def run(page: Page, index) -> None:

    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)

    
    # classURL = f'./ultra/courses/'
    # classUrlUltra = f'{classURL}{id_interno}/outline'
    # classBulkEdit = f'{classUrlUltra}/bulkEditContent'

    print(id_externo)

    # await page.goto(classBulkEdit)

    await AjusteDataFael.ajusteData(page=page, id_interno=id_interno, data1='18/09/25', data2='10/09/25', data3='20/08/25')
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()


asyncio.run(main())