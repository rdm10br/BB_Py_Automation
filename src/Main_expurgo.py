import asyncio
from playwright.async_api import Page
 
 
from Metodos import getPlanilha, getFromAPI, Expurgo
from Decorators import playwright_StartUp_nosub_expurgo
 
 
@playwright_StartUp_nosub_expurgo()
async def run(page: Page, index) -> None:
 
    id_externo = getPlanilha.getCell_expurgo(index=index)
    id_interno = await getFromAPI.API_Req_expurgo(page=page, id_externo=id_externo)
    id_user = getPlanilha.getUser(index=index)
    list_user = getPlanilha.list_expurgo_user
 
    print(id_externo)
 
    await Expurgo.expurgo_root(page=page, id_interno=id_interno, id_user=id_user)
    getPlanilha.writeOnExcel_Plan3(index=index, return_status='OK')
    
    print(id_user)
 
async def main():
    await run()
 
 
asyncio.run(main())