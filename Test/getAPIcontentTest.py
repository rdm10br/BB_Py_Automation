import asyncio, json, typing, pytz
from datetime import datetime
from playwright.async_api import (async_playwright, expect, Page)


async def API_Config(page: Page,
    id_interno: str,
    item_Search: typing.Optional[typing.Literal[
        'Fórum de Interação entre Professores e Tutores',
        'Meu Desempenho',
        'Organize seus estudos com a Sofia',
        'Fale com o Tutor',
        'Desafio Colaborativo',
        'Unidade 1',
        'Unidade 2',
        'Unidade 3',
        'Unidade 4',
        'Atividade Contextualizada',
        'Relatório de Aulas Práticas',
        'WebAula',
        'Avaliações',
        'Solicite seu livro impresso',
        'SER Melhor (Clique Aqui para deixar seu elogio,'\
        ' crítica ou sugestão)',
        'AV1',
        'AV2',
        'AF',
        'Avaliação On-Line 1 (AOL 1) - Questionário',
        'Avaliação On-Line 2 (AOL 2) - Questionário',
        'Avaliação On-Line 3 (AOL 3) - Questionário',
        'Avaliação On-Line 4 (AOL 4) - Questionário',
        'Avaliação On-Line 5 (AOL 5) - Atividade Contextualizada',
        'Atividade de Autoaprendizagem 1',
        'Atividade de Autoaprendizagem 2',
        'Atividade de Autoaprendizagem 3',
        'Atividade de Autoaprendizagem 4',
        'Material Didático Interativo',
        'Biblioteca Virtual: e-Book',
        'Videoteca: Videoaulas']] = None,
    config: typing.Optional[typing.Literal[
        'visible',
        'visibleInBook',
        'multipleAttempts',
        'aggregationModel',
        'possible',
        'availability.available',
        'genericReadOnlyData.dueDate',
        'aggregationModel',
        'contentDetail["resource/x-bb-asmt-test-link"].test.assessment.id',
        'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfQuestionsRequired',
        'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfAnswersRequired',
        'contentDetail["resource/x-bb-externallink"].url',
        'contentDetail["resource/x-bb-blti-link"].url',
        'contentHandler.url',
        'description']] = None ) -> str:
    
    """_summary_

    Args:
        page (Page): _description_
        id_interno (str): _description_
        item_Search (_type_, optional): _description_. Defaults to None.
        config (typing.Optional[typing.Literal[ &#39;visible&#39;, &#39;visibleInBook&#39;, &#39;multipleAttempts&#39;, &#39;aggregationModel&#39;, &#39;possible&#39;, &#39;availability.available&#39;, &#39;genericReadOnlyData.dueDate&#39;, &#39;aggregationModel&#39;, &#39;contentDetail[&quot;resource, optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    
    baseURL = 'https://sereduc.blackboard.com/'
    # id_externo=''
    # externalID_API = f'{baseURL}learn/api/public/v1/courses/externalId:{id_externo}/contents'
    internalID_API = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents'''
    
    # father_id = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents'''
    # id_atividade = internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children?title={item_Search}'
    # APIGradeCollum = f'{baseURL}learn/api/v1/courses/{id_interno}/gradebook/columns'
    # id_assesment = APIAssesmentID = f'''{baseURL}learn/api/v1/courses/{id_interno}/contents/{id_atividade}/children'''
    # id_encapsulamento = APIEncapsulamento = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{id_assesment}/questions/'''
    # APIBQItem = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{id_assesment}/questions/{id_encapsulamento}/questions?expand=sourceInfo'''
    
    
    filteredRequest_title = f'''function getFilteredResults(){{
    const data = JSON.parse(document.body.innerText).results;
    const filteredResults = data.filter(item => item.title === "{item_Search}")[0].{config};
    return filteredResults;}}'''
    
    filteredRequest_name = f'''function getFilteredResults(){{
    const data = JSON.parse(document.body.innerText).results;
    const filteredResults = data.filter(item => item.name === "{item_Search}")[0].{config};
    return filteredResults;}}'''
    
    filteredRequest_columnName = f'''function getFilteredResults(){{
    const data = JSON.parse(document.body.innerText).results;
    const filteredResults = data.filter(item => item.columnName === "{item_Search}")[0].{config};
    return filteredResults;}}'''
    
    print(f'Looking on Api Content for {item_Search} config {config} in'\
          f'{id_interno}')
    
    await page.goto(url=internalID_API, wait_until='networkidle')
    
    result = await page.evaluate(filteredRequest_title)
    
    return result


async def date_adjust(utc_time_str: str):
    """_summary_

    Args:
        utc_time_str (str): _description_

    Returns:
        _type_: _description_
    """
    
    # Define the UTC time string
    # utc_time_str = '2024-06-11T02:59:59.999Z'

    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    utc_time = utc_time.replace(tzinfo=pytz.UTC)

    local_tz = pytz.timezone('America/Recife')
    local_time = utc_time.astimezone(local_tz)

    # Format the local time as desired
    #formatted_local_time = local_time.strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
    formatted_local_time = local_time.strftime('%d/%m/%Y %H:%M')
    print("Formatted Local Time:", formatted_local_time)
    
    return formatted_local_time


async def main():
    async with async_playwright() as playwright:
        
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        CACHE_FILE = r'Metodos\Login\__pycache__\login_cache.json'
        with open(CACHE_FILE, 'r') as f:
            cache_data = json.load(f)
        await page.context.add_cookies(cache_data['cookies'])
        
        baseURL = "https://sereduc.blackboard.com/"
        id_interno = '_187869_1'
        
        await page.goto(baseURL)
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_timeout(5000)
        
        teste = await API_Config(page=page, id_interno=id_interno, item_Search='Solicite seu livro impresso', config='contentHandler.url')
        
        print(teste)


if __name__ == "__main__":
    asyncio.run(main())