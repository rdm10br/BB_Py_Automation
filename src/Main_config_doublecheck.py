import asyncio
from playwright.async_api import Page


from Metodos import getPlanilha, getFromAPI, getAPIContentConfig
from Decorators.Main_StartUp import playwright_StartUp_nosub


@playwright_StartUp_nosub
async def run(page: Page, index) -> None:
    
        id_externo = getPlanilha.getCell(index=index)
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        
        # classURL = f'{baseURL}ultra/courses/'
        # classUrlUltra = f'{classURL}{id_interno}/outline'
        
        print(id_externo)
        
        # Masters DIG e TRAD
        result  =  await getAPIContentConfig.doublecheck_config_main_Master(page=page, id_interno=id_interno, index=index)
        #=======================================================================
        
        # Mescla/Master DIG
        # result  =  await getAPIContentConfig.doublecheck_config_main_DIG(page=page, id_interno=id_interno, index=index)
        #=======================================================================
        
        # Mescla/Master TRAD
        # result  =  await getAPIContentConfig.doublecheck_config_main_TRAD(page=page, id_interno=id_interno, index=index)
        #=======================================================================
        
        # Master MEC
        # result  = await getAPIContentConfig.doublecheck_config_main_MEC(page=page, id_interno=id_interno, index=index)
        #=======================================================================
        
        print(result)
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
        getPlanilha.writeOnExcel_Plan1_Result(index=index, return_status=result)

        
async def main():
    await run()


asyncio.run(main())