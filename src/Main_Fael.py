import asyncio
from Decorators.Main_StartUp import playwright_StartUp
from playwright.async_api import Page

from Metodos import Fael, getPlanilha, getFromAPI, ajuste_AV1, AjusteDataFael, grupo_fael

@playwright_StartUp()
async def main(page: Page, index) -> None:
   
    # Recuperando o id_externo da planilha
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    # Passando o id_externo como 'id_interno' para a função ajusteGradebook
    print("Iniciando ajusteGradebook...")
    await Fael.ajusteGradebook(page, id_interno)  # Passando id_externo como id_interno
    await ajuste_AV1.ajusteFael(page, id_interno)
    
    # data1 : str, optional
    # description: Defaults to '17/05/25', this date changes the due date to [Exercício de Fixação 01, 02, 03, Exercício do Conhecimento] and Ending date [Fale com o tutor].

    # data2 : str, optional
    # description: Defaults to '10/05/25', this date changes the due date to [Avaliação Workshop, Discursiva] and Ending date [Converse com a sua Turma]

    # data3 : str, optional
    # description: Defaults to '20/04/25', this date changes the Opening date to [Avaliação Workshop]
    await AjusteDataFael.ajusteData(page, id_interno, data1='17/05/25', data2='10/05/25', data3='20/04/25')
    
    await grupo_fael.inserirArquivo(page, id_interno)
    await grupo_fael.atribuirGruposFael(page, id_interno)
    
    getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    print("Finalizando ajusteGradebook.")
    
asyncio.run(main())  # Rodar sem o decorator