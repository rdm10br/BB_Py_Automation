import asyncio
from playwright.async_api import Page

from Decorators import playwright_StartUp
from Metodos import Fael, getPlanilha, getFromAPI, ajuste_AV1, AjusteDataFael, grupo_fael

@playwright_StartUp()
async def main(page: Page, index) -> None:
   
    # Recuperando o id_externo da planilha
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    # Lembrar de alterar a data para as engenharias  e serviços sociais (RODAR SEPARADO)
    dataI: list[str] = ['16/08/25',
                        '16/10/25',
                        '01/09/25',
                        '01/11/25']
    dataF: list[str] = ['16/10/25',
                        '30/11/25',
                        '15/10/25',
                        '29/11/25']
    await AjusteDataFael.ajusteData_estag(page, id_interno, dataI=dataI, dataF=dataF)
    
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    print("Finalizando ajusteGradebook.")
    
asyncio.run(main())  # Rodar sem o decorator