import asyncio
from playwright.async_api import Page

from Decorators import playwright_StartUp
from Metodos import getPlanilha, getFromAPI, limpar_sala

@playwright_StartUp()
async def main(page: Page, index) -> None:
   
    # Recuperando o id_externo da planilha
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    await limpar_sala.limpar_sala_root(page=page, id_interno=id_interno)
    
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    
async def _main():
    await main()
    # os.system("shutdown /s /t 0")


asyncio.run(_main())