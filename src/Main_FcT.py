import asyncio
from playwright.async_api import Page
 
 
from Metodos import getPlanilha, getFromAPI, falecomtutor
from Decorators.Main_StartUp import playwright_StartUp_nosub
 
 
@playwright_StartUp_nosub
async def run(page: Page, index) -> None:
 
    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)
 
    print(id_externo)
 
    await falecomtutor.falecomtutor(page=page, id_interno=id_interno)
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
 
 
async def main():
    await run()
 
 
asyncio.run(main())