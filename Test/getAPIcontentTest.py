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
        'SER Melhor (Clique Aqui para deixar seu elogio, crítica ou sugestão)',
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
        'Videoteca: Videoaulas']] = None) -> str:

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
        'description']] = None
    
    baseURL = 'https://sereduc.blackboard.com/'
    internalID_API = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents'''
    APIGradeCollum = f'''{baseURL}learn/api/v1/courses/{id_interno}/gradebook/columns'''
    
    # id_externo=''
    # externalID_API = f'{baseURL}learn/api/public/v1/courses/externalId:{id_externo}/contents'

    father_id = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents'''
    # internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children?title={item_Search}'->id_atividade
    # APIAssesmentID = f'''{baseURL}learn/api/v1/courses/{id_interno}/contents/{id_atividade}/children'''->id_assesment
    # APIEncapsulamento = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{id_assesment}/questions/'''->id_encapsulamento
    # APIBQItem = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{id_assesment}/questions/{id_encapsulamento}/questions?expand=sourceInfo'''->BQ associado

    def filteredRequest_title(item_search: str, config: str):
        request = f'''function getFilteredResults(){{const data = JSON.parse(document.body.innerText).results;
        const filteredResults = data.filter(item => item.title === "{item_Search}")[0].{config};
        return filteredResults;}}'''
        return request

    def filteredRequest_name(item_search: str, config: str):
        request= f'''function getFilteredResults(){{
        const data = JSON.parse(document.body.innerText).results;
        const filteredResults = data.filter(item => item.name === "{item_Search}")[0].{config};
        return filteredResults;}}'''
        return request

    def filteredRequest_columnName(item_search: str, config: str):
        request= f'''function getFilteredResults(){{
        const data = JSON.parse(document.body.innerText).results;
        const filteredResults = data.filter(item => item.columnName === "{item_Search}")[0].{config};
        return filteredResults;}}'''
        return request

    # print(f'Looking on Api Content for {item_Search} config {config} in'
    #       f'{id_interno}')
    # await page.goto(url=internalID_API, wait_until='networkidle')
    # result = await page.evaluate(filteredRequest_columnName(item_Search, config))
    # return result
    
    match item_Search:
        case 'Fórum de Interação entre Professores e Tutores':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Meu Desempenho':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #Verificar se o link está correto
            
            return result, result2
        case 'Organize seus estudos com a Sofia':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #Verificar se o link está correto
            
            return result, result2
        case 'Fale com o Tutor':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Desafio Colaborativo':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #verificar se está com os grupos
            
            return result
        case 'Unidade 1':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Unidade 2':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Unidade 3':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Unidade 4':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Material Didático Interativo':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #verificar validade do link
            
            return result, result2
        case 'Videoteca: Videoaulas':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #verificar validade do link
            
            return result, result2
        case 'Biblioteca Virtual: e-Book':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #verificar validade do link
            
            return result, result2
        case 'WebAula':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Avaliações':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'Atividade Contextualizada':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            return result
        case 'AV1':
            await page.goto(url=APIGradeCollum, wait_until='networkidle')
            
            config = 'genericReadOnlyData.dueDate'
            print(f'Checking {item_Search} hand in date...')
            result = await page.evaluate(filteredRequest_columnName(item_Search, config))
            
            #other configs
            
            return result
        case 'AV2':
            await page.goto(url=APIGradeCollum, wait_until='networkidle')
            
            result = await page.evaluate(filteredRequest_columnName(item_Search, config))
            
            #other configs
            
            return result
        case 'AF':
            await page.goto(url=APIGradeCollum, wait_until='networkidle')
            
            result = await page.evaluate(filteredRequest_columnName(item_Search, config))
            
            #other configs
            
            return result
        case 'SER Melhor (Clique Aqui para deixar seu elogio, cr…':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #Verificar se o link está correto
            
            return result, result2
        case 'Solicite seu livro impresso':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #Verificar se o link está correto
            
            return result, result2
        case 'Relatório de Aulas Práticas':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #other configs
            
            return result
        case 'Atividade de Autoaprendizagem 1':
            #all configs
            return result
        case 'Atividade de Autoaprendizagem 2':
            #all configs
            return result
        case 'Atividade de Autoaprendizagem 3':
            #all configs
            return result
        case 'Atividade de Autoaprendizagem 4':
            #all configs
            return result
        case 'Avaliação On-Line 1 (AOL 1) - Questionário':
            #all configs
            return result
        case 'Avaliação On-Line 2 (AOL 2) - Questionário':
            #all configs
            return result
        case 'Avaliação On-Line 3 (AOL 3) - Questionário':
            #all configs
            return result
        case 'Avaliação On-Line 4 (AOL 4) - Questionário':
            #all configs
            return result
        case 'Avaliação On-Line 5 (AOL 5) - Atividade Contextual…':
            #all configs
            
            # config = 'genericReadOnlyData.dueDate'
            # print(f'Checking {item_Search} hand in date...')
            # result = await page.evaluate(filteredRequest_title(item_Search, config))

            return result
        case _:
            result = f'Item ({item_Search}) não encontrado ou nomeclatura errada'
            print(result)
            return result


async def date_adjust(utc_time_str: str):

    # Define the UTC time string
    # utc_time_str = '2024-06-11T02:59:59.999Z'

    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    utc_time = utc_time.replace(tzinfo=pytz.UTC)

    local_tz = pytz.timezone('America/Recife')
    local_time = utc_time.astimezone(local_tz)

    # Format the local time as desired
    # formatted_local_time = local_time.strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
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

        baseURL = 'https://sereduc.blackboard.com/'
        id_interno = '_187869_1'

        await page.goto(baseURL)
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_timeout(5000)

        visibility, item_URL = await API_Config(page=page, id_interno=id_interno, item_Search='Meu Desempenho')
        await page.wait_for_timeout(5*1000)
        print(visibility, item_URL)


if __name__ == "__main__":
    asyncio.run(main())