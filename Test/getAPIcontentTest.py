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
        'id',
        'score.possible',
        'availability.available',
        'genericReadOnlyData.dueDate',
        'grading.scoringModel',
        'contentDetail["resource/x-bb-asmt-test-link"].test.assessment.id',
        'contentHandler.assessmentId',
        'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfQuestionsRequired',
        'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfAnswersRequired',
        'contentDetail["resource/x-bb-externallink"].url',
        'contentDetail["resource/x-bb-blti-link"].url',
        'contentHandler.url',
        'description']] = None
    
    baseURL = 'https://sereduc.blackboard.com/'
    internalID_API = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents'''
    APIGradeCollum = f'''{baseURL}learn/api/v1/courses/{id_interno}/gradebook/columns'''
    APIGradeColumn = f'''{baseURL}learn/api/public/v2/courses/{id_interno}/gradebook/columns'''
    
    def APIFolder(father_id: str):
        API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children'
        return API
    
    # id_externo=''
    # externalID_API = f'{baseURL}learn/api/public/v1/courses/externalId:{id_externo}/contents'
    
    id_discussion = '' #f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents'+'JSON.parse(document.body.innerText).results[1].contentHandler.targetId'
    discussionGroups = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{id_discussion}/groups'
    groupsID = f'{baseURL}learn/api/public/v2/courses/{id_interno}/groups/sets'
    req_len = 'JSON.parse(document.body.innerText).results.length' #to see request length, especially groups
    
    # father_id = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents'''
    # internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children?title={item_Search}'->id_atividade
    # APIAssesmentID = f'''{baseURL}learn/api/v1/courses/{id_interno}/contents/{id_atividade}/children'''->id_assesment
    # APIEncapsulamento = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{id_assesment}/questions/'''->id_encapsulamento
    # APIBQItem = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{id_assesment}/questions/{id_encapsulamento}/questions?expand=sourceInfo'''->BQ associado

    # JSON.parse(document.body.innerText).results.filter(item => item.title === "{item_Search}")[0].{config}
    def filteredRequest_title(item_search: str, config: str):
        request = f'''JSON.parse(document.body.innerText).results.filter(item => item.title === "{item_search}")[0].{config}'''
        return request

    def filteredRequest_name(item_search: str, config: str):
        request= f'''JSON.parse(document.body.innerText).results.filter(item => item.name === "{item_search}")[0].{config}'''
        return request

    def filteredRequest_columnName(item_search: str, config: str):
        request= f'''JSON.parse(document.body.innerText).results.filter(item => item.columnName === "{item_search}")[0].{config}'''
        return request
    
    async def check_item_all_folders_unidade():
        
        results = ''
        id_folder: list = []

        await page.goto(url=internalID_API, wait_until='networkidle')

        for index in range(4):
            index+=1
            config = 'id'
            unidade = f'Unidade {index}'
            print(f'Checking Unidade {index} id...')
            id_value = await page.evaluate(filteredRequest_title(item_search=unidade, config=config))
            id_folder.append(id_value)
            print(id_folder[index-1])
        
        for i in range(4):
            
            await page.goto(url=APIFolder(id_folder[i]), wait_until='networkidle')
            i+=1
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result1 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #verificar validade do link
            
            results = f'{results}{item_Search} from Unidade {i} : visibility: {result1} | URL: {result2}\n'
        
        return results

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
            
            results = f'{item_Search}: visibility: {result} | URL: {result2}'
            return results
        
        case 'Organize seus estudos com a Sofia':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #Verificar se o link está correto
            
            results = f'{item_Search}: visibility: {result} | URL: {result2}'
            return results
        
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
            
            results = ''
            id_folder: list = []

            await page.goto(url=internalID_API, wait_until='networkidle')

            for index in range(4):
                index+=1
                config = 'id'
                unidade = f'Unidade {index}'
                print(f'Checking Unidade {index} id...')
                id_value = await page.evaluate(filteredRequest_title(item_search=unidade, config=config))
                id_folder.append(id_value)
                print(id_folder[index-1])
            
            for i in range(4):
                
                await page.goto(url=APIFolder(id_folder[i]), wait_until='networkidle')
                i+=1
                
                config = 'availability.available'
                print(f'Checking {item_Search} visibility...')
                result1 = await page.evaluate(filteredRequest_title(item_Search, config))
                
                config = 'contentHandler.url'
                print(f'Checking {item_Search} associated URL...')
                result2 = await page.evaluate(filteredRequest_title(item_Search, config))
                
                #verificar validade do link
                
                results = f'{results}{item_Search} from Unidade {i} : visibility: {result1} | URL: {result2}\n'
            
            return results
        
        case 'Videoteca: Videoaulas':
            
            results = ''
            id_folder: list = []

            await page.goto(url=internalID_API, wait_until='networkidle')

            for index in range(4):
                index+=1
                config = 'id'
                unidade = f'Unidade {index}'
                print(f'Checking Unidade {index} id...')
                id_value = await page.evaluate(filteredRequest_title(item_search=unidade, config=config))
                id_folder.append(id_value)
                print(id_folder[index-1])
            
            for i in range(4):
                
                await page.goto(url=APIFolder(id_folder[i]), wait_until='networkidle')
                i+=1
                
                config = 'availability.available'
                print(f'Checking {item_Search} visibility...')
                result1 = await page.evaluate(filteredRequest_title(item_Search, config))
                
                config = 'contentHandler.url'
                print(f'Checking {item_Search} associated URL...')
                result2 = await page.evaluate(filteredRequest_title(item_Search, config))
                
                #verificar validade do link
                
                results = f'{results}{item_Search} from Unidade {i} : visibility: {result1} | URL: {result2}\n'
            
            return results
        
        case 'Biblioteca Virtual: e-Book':
            
            results = ''
            id_folder: list = []
            
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            for index in range(4):
                index+=1
                config = 'id'
                unidade = f'Unidade {index}'
                print(f'Checking Unidade {index} id...')
                id_value = await page.evaluate(filteredRequest_title(item_search=unidade, config=config))
                id_folder.append(id_value)
                print(id_folder[index-1])
            
            for i in range(4):
                
                await page.goto(url=APIFolder(id_folder[i]), wait_until='networkidle')
                i+=1
                
                config = 'availability.available'
                print(f'Checking {item_Search} visibility...')
                result1 = await page.evaluate(filteredRequest_title(item_Search, config))
                
                config = 'contentHandler.url'
                print(f'Checking {item_Search} associated URL...')
                result2 = await page.evaluate(filteredRequest_title(item_Search, config))
                
                #verificar validade do link
                
                results = f'{results}{item_Search} from Unidade {i} : visibility: {result1} | URL: {result2}\n'
            
            return results
        
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
            
            #configs valor da note, nomeclatura certa, se está visivel para o aluno
            
            return result
        
        case 'SER Melhor (Clique Aqui para deixar seu elogio, crítica ou sugestão)':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #Verificar se o link está correto
            
            results = f'{item_Search}: visibility: {result} | URL: {result2}'
            return results
        
        case 'Solicite seu livro impresso':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))
            
            #Verificar se o link está correto
            
            results = f'{item_Search}: visibility: {result} | URL: {result2}'
            return results
        
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
            #all configsl
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

        # visibility, item_URL = await API_Config(page=page, id_interno=id_interno, item_Search='Meu Desempenho')
        # visibility, item_URL = await API_Config(page=page, id_interno=id_interno, item_Search='SER Melhor (Clique Aqui para deixar seu elogio, crítica ou sugestão)')
        result = await API_Config(page=page, id_interno=id_interno, item_Search='Material Didático Interativo')
        await page.wait_for_timeout(5*1000)
        # print(visibility, item_URL)
        print(result)


if __name__ == "__main__":
    asyncio.run(main())