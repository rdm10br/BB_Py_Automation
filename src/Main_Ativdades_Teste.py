import asyncio, time, json
from playwright.async_api import Page
from Metodos import getPlanilha, getFromAPI, gruposAtividades, AjusteNotaZero
from Decorators.Main_StartUp import playwright_StartUp

@playwright_StartUp
async def run(page: Page, index) -> None:
    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    
    classURL = f'./ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'
    
    print(id_externo)
    
    await page.goto(classUrlUltra)
    
    await AjusteNotaZero.AjusteNotaZero(page=page, id_interno=id_interno)
    
    course_area = await getFromAPI.API_Ativ_Course(page=page, id_externo=id_externo)
    
    COURSE_MAPPING = r'src\Json\course_mapping.json'

    with open(COURSE_MAPPING, 'r', encoding='utf-8') as f:
        course_mapping = json.load(f)
    
    async def process_courses(page: Page, id_interno: str, course_area: str, cursos: list, index: int):
        await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
        print(course_area)
        
        start_time0 = time.time()
        for curso in cursos:
            await gruposAtividades.inserirGruposAtividadesAV1(page=page, id_interno=id_interno, curso=curso)
            await page.wait_for_load_state('load')
            await gruposAtividades.inserirGruposAtividadesAV2(page=page, id_interno=id_interno, curso=curso)
            await page.wait_for_load_state('load')
        end_time0 = time.time()
        execution_time = end_time0 - start_time0
        executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
        print(executionTime0)
        
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    
    if course_area in course_mapping:
        await process_courses(page, id_interno, course_area, course_mapping[course_area], index)
    else:
        print(f'Grande Área da sala {id_externo} não identificada; {course_area}')
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='Não identificado')


async def main():
    await run()

asyncio.run(main())