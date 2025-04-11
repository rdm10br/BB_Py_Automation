import asyncio
from Decorators.Main_StartUp import playwright_StartUp_nosub
from playwright.async_api import Page
from Metodos import Fael, getPlanilha, getFromAPI, ajuste_AV1

@playwright_StartUp_nosub()
async def main(page: Page, index) -> None:
   
    # Recuperando o id_externo da planilha
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    # Passando o id_externo como 'id_interno' para a função ajusteGradebook
    print("Iniciando ajusteGradebook...")
    await Fael.ajusteGradebook(page, id_interno)  # Passando id_externo como id_interno
    await ajuste_AV1.ajusteFael(page, id_interno)
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    print("Finalizando ajusteGradebook.")
    
asyncio.run(main())  # Rodar sem o decorator