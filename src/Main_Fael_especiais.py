import asyncio
from playwright.async_api import Page

from Decorators import playwright_StartUp
from Metodos import Fael, getPlanilha, getFromAPI, ajuste_AV1, AjusteDataFael, grupo_fael

@playwright_StartUp(autoSub=True)
async def main(page: Page, index) -> None:
   
    # Recuperando o id_externo da planilha
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    # Passando o id_externo como 'id_interno' para a função ajusteGradebook
    print("Iniciando ajusteGradebook...")
    # await Fael.ajusteGradebook(page, id_interno)  # Passando id_externo como id_interno
    await ajuste_AV1.ajusteFael(page, id_interno)
    
    # Lembrar de alterar a data para as engenharias (RODAR SEPARADO)
    dataI1: list[str] = ['25/08/25', '15/09/25', '06/10/25', '27/10/25'] # etapa 1
    dataF1: list[str] = ['05/09/25', '25/09/25', '17/10/25', '10/11/25']
    dataI2: list[str] = ['17/11/25', '01/12/25'] # etapa 2
    dataF2: list[str] = ['30/11/25', '28/12/25']
    await AjusteDataFael.ajusteData_especiais(page, id_interno, dataI1=dataI1, dataF1=dataF1, dataI2=dataI2, dataF2=dataF2)
    
    await grupo_fael.inserirArquivo(page, id_interno)
    # await grupo_fael.atribuirGruposFael(page, id_interno)
    
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    print("Finalizando ajusteGradebook.")
    
asyncio.run(main())  # Rodar sem o decorator