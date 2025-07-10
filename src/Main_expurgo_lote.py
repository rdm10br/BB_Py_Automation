import asyncio
from playwright.async_api import Page
 
 
from Metodos import getPlanilha, getFromAPI, Expurgo
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index) -> None:
 
    id_externo = getPlanilha.getCell_expurgo(index=index)
    id_interno = await getFromAPI.API_Req_expurgo(page=page, id_externo=id_externo)
    id_user = getPlanilha.getUser(index=index)
    list_user = str(list(getPlanilha.list_expurgo_user['USER'].values)[0]).split(',')
 
    print(id_externo)
    # print(id_user)
    # print(list_user)
    
    # await Expurgo.expurgo_root(page=page, id_interno=id_interno, id_user=id_user)
    await Expurgo.expurgo_root_lote(page=page, id_interno=id_interno, id_user=list_user)
    getPlanilha.writeOnExcel_Plan3(index=index, return_status='OK')
    
    print(id_user)
 
async def main():
    await run()
 
 
asyncio.run(main())