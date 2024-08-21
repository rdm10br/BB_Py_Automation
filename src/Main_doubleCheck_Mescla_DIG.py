import asyncio
from playwright.async_api import Page, expect


from Metodos import getPlanilha, getFromAPI, atribGrup, AjusteNotaZero, AjusteAvaliacaoV2
from Decorators.Main_StartUp import playwright_StartUp


@playwright_StartUp
async def run(page: Page, index) -> None:
    
        id_externo = getPlanilha.getCell(index=index)
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        
        classURL = f'./ultra/courses/'
        classUrlUltra = f'{classURL}{id_interno}/outline'
        
        print(id_externo)
        
        await page.goto(classUrlUltra)
        
        # VETERANOS
        # await atribGrup.inserirArquivoVET(page=page, id_interno=id_interno)
        # await atribGrup.atribuirGruposVET(page=page, id_interno=id_interno)
        #===================
        
        # DIGITAL
        await atribGrup.inserirArquivoDIG(page=page, id_interno=id_interno)
        await atribGrup.atribuirGruposDIG(page=page, id_interno=id_interno)
        #===================
        
        await AjusteNotaZero.AjusteNotaZero(page=page, id_interno=id_interno)
        await AjusteAvaliacaoV2.ajusteAvaliacao(page=page, id_interno=id_interno)
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')


async def main():
    await run()


asyncio.run(main())