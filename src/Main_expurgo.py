import asyncio
from playwright.async_api import Page
 
 
from Metodos import getPlanilha, getFromAPI, DoubleCheckDB, Expurgo
from Decorators.Main_StartUp import playwright_StartUp_nosub_expurgo
 
 
@playwright_StartUp_nosub_expurgo()
async def run(page: Page, index) -> None:
 
    id_externo = getPlanilha.getCell_expurgo(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    id_user = getPlanilha.getUser(index=index)
 
    print(id_externo)
 
    await Expurgo.expurgo(page=page, id_interno=id_interno, id_user=id_user)
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    
    print(id_user)
 
async def main():
    await run()
 
 
asyncio.run(main())