import asyncio
from playwright.async_api import Page, expect


from Metodos import getPlanilha, getFromAPI, getAPIContentConfig
from Decorators.Main_StartUp import playwright_StartUp


@playwright_StartUp
async def run(page: Page, index) -> None:
    
        id_externo = getPlanilha.getCell(index=index)
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        # baseURL = 'https://sereduc.blackboard.com/'
        # classURL = f'{baseURL}ultra/courses/'
        # classUrlUltra = f'{classURL}{id_interno}/outline'
        
        print(id_externo)
        
        # Masters DIG e TRAD
        # result  =  await getAPIContentConfig.doublecheck_config_main_Master(page=page, id_interno=id_interno)

        # Mescla/Master DIG
        # result  =  await getAPIContentConfig.doublecheck_config_main_DIG(page=page, id_interno=id_interno)

        # Mescla/Master TRAD
        # result  =  await getAPIContentConfig.doublecheck_config_main_TRAD(page=page, id_interno=id_interno)
        
        # Master MEC
        result  = await getAPIContentConfig.doublecheck_config_main_MEC(page=page, id_interno=id_interno)
        
        print(result)
        # getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')

        
async def main():
    await run()


asyncio.run(main())