import asyncio, pytz, json
from datetime import datetime
from playwright.async_api import async_playwright, expect, Page

async def API_Config(page: Page, id_interno: str, item_Search: str) -> str:

    baseURL = 'https://sereduc.blackboard.com/'
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents'
    internalID_API_noPublic = f'{baseURL}learn/api/v1/courses/{id_interno}/contents'
    APIGradeCollum = f'{baseURL}learn/api/v1/courses/{id_interno}/gradebook/columns'

    def APIFolder_noPublic(fatherID: str):
        API = f'{baseURL}learn/api/v1/courses/{id_interno}/contents/{fatherID}/children'
        return API
    
    def APIFolder(father_id: str):
        API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children'
        return API

    def request_unfiltered_noResults(config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText);
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('item not found in room {id_interno}');
                }}
            }}'''
        return request
    
    def request_unfiltered(config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results;
            if (data && data.{config}) {{
                return data.{config};
            }} else {{
                throw new Error('item not found in room {id_interno}');
                }}
            }}'''
        return request
    
    def request_unfiltered_toString(config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results;
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('item not found in room {id_interno}');
                }}
            }}'''
        return request
    
    def request_unfiltered0(config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results[0];
            if (data && data.{config}) {{
                return data.{config};
            }} else {{
                throw new Error('item not found in room {id_interno}');
                }}
            }}'''
        return request

    def filteredRequest_title(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.title === "{item_search}");
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('{item_search} not found in room {id_interno}');
                }}
            }}'''
        return request

    def filteredRequest_name(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.name === "{item_search}");
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('{item_search} not found in room {id_interno}');
                }}
            }}'''
        return request

    def filteredRequest_columnName(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.columnName === "{item_search}");
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('{item_search} not found in room {id_interno}');
                }}
            }}'''
        return request

    async def check_item_in_all_folders_unidade(item_search: str):
        results = ''
        id_folder: list = []

        await page.goto(url=internalID_API, wait_until='networkidle')

        for index in range(4):
            index += 1
            config = 'id'
            unidade = f'Unidade {index}'
            print(f'Checking Unidade {index} id...')
            id_value = await page.evaluate(filteredRequest_title(item_search=unidade, config=config))
            id_folder.append(id_value)
            print(id_folder[index-1])

        for i in range(4):
            await page.goto(url=APIFolder(id_folder[i]), wait_until='networkidle')
            i += 1

            config = 'availability.available'
            print(f'Checking {item_search} visibility...')

            try:
                result_visibility = await page.evaluate(filteredRequest_title(item_search, config))
            except Exception as e:
                if f'{item_search} not found in room {id_interno}' in str(e):
                    print(f'Erro na sala: {id_interno}; Item: {item_search} não foi encontrado')
                    continue
                else:
                    print('Erro ao processar request:', e)
                    continue
            config = 'contentHandler.url'
            print(f'Checking {item_search} associated URL...')

            try:
                result_url = await page.evaluate(filteredRequest_title(item_search, config))
                if result_url == 'https://www.sereducacional.com' or result_url == 'https://www.sereducacional.com/':
                    result_url = f'{result_url} is wrong! | there is no content in {item_search} from Unidade {i}!'
            except Exception as e:
                if f'{item_search} not found in room {id_interno}' in str(e):
                    print(f'Erro na sala: {id_interno}; Item: {item_search} não foi encontrado')
                    continue
                else:
                    print('Erro ao processar request:', e)
                    continue

            # verificar validade do link

            if result_visibility != f'{item_search} not found in room {id_interno}':
                results = f'{results}{item_Search} from Unidade {i} : visibility: {result_visibility} | URL: {result_url}\n'
            else:
                results = f'{results}{item_search} não encontrado na Unidade {i}\n'

        return results

    async def activity_configs(item_search: str): #
        
        #API Grade configs
        await page.goto(url=APIGradeCollum, wait_until='commit')
        
        config = 'visible'
        print(f'Checking {item_search} visible...')
        result_visibility = await page.evaluate(filteredRequest_columnName(item_search, config))
        # "visible": true,

        config = 'possible'
        print(f'Checking {item_search} possible...')
        result_possible_note = await page.evaluate(filteredRequest_columnName(item_search, config))
        # "possible": 10,

        config = 'multipleAttempts'
        print(f'Checking {item_search} possible...')
        result_attempts = await page.evaluate(filteredRequest_columnName(item_search, config))
        # "multipleAttempts": 0,

        config = 'visibleInBook'
        print(f'Checking {item_search} visibleInBook...')
        result_visibleInBook = await page.evaluate(filteredRequest_columnName(item_search, config))
        # "visibleInBook": false,
        
        config = 'aggregationModel'
        print(f'Checking {item_search} aggregationModel...')
        result_aggregationModel = await page.evaluate(filteredRequest_columnName(item_search, config))
        # "aggregationModel": "HIGHEST",'
        
        # config = 'genericReadOnlyData.dueDate'
        config = 'dueDate'
        print(f'Checking {item_search} hand in date...')
        
        try:
            result_dueDate = await page.evaluate(filteredRequest_columnName(item_search, config))
        except Exception as e:
            result_dueDate = 'No date associated!'
        
        if result_dueDate != 'No date associated!':
            result_dueDate = await adjust_date(result_dueDate)
        
        # verificar depois, erro desconhecido, sala 1 de testes não funciona, sala 2 de testes funciona
        # config = 'description'
        # print(f'Checking {item_search} description...')
        # result_description = await page.evaluate(filteredRequest_columnName(item_search, config))
        #=======================================================================
        
        #API contents
        await page.goto(url=internalID_API, wait_until='commit')
        
        search_item = ''.join([ch for ch in item_search if ch.isdigit()])
        
        match search_item[0]:
            case '1' :
                item = 'Unidade 1'
            case '2' :
                item = 'Unidade 2'
            case '3' :
                item = 'Unidade 3'
            case '4' :
                item = 'Unidade 4'
        
        config = 'id'
        folderID = await page.evaluate(filteredRequest_title(item_search=item, config=config))
        
        await page.goto(url=APIFolder_noPublic(folderID), wait_until='commit')
        
        try:
            config = 'contentDetail["resource/x-bb-asmt-test-link"].test.assessment.id'
            itemID = await page.evaluate(filteredRequest_title(item_search=item_Search, config=config))
            
            if itemID != f'{item_search} not found in room {id_interno}':
                
                config = 'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfAnswersRequired'
                print(f'Checking {item_search} Randomization of Answers Required...')
                result_isRandomizationOfAnswersRequired = await page.evaluate(filteredRequest_columnName(item_search, config))
                
                if result_isRandomizationOfAnswersRequired == "ALWAYS":
                    result_isRandomizationOfAnswersRequired = f'{item_search} is set to always ramdomize Answers'
                else:
                    result_isRandomizationOfAnswersRequired = f'{item_search} is not set to always ramdomize Answers'
                
                config = 'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfQuestionsRequired'
                print(f'Checking {item_search} Randomization of Questions Required...')
                result_isRandomizationOfQuestionsRequired = await page.evaluate(filteredRequest_columnName(item_search, config))
                
                if result_isRandomizationOfQuestionsRequired == "true":
                    result_isRandomizationOfQuestionsRequired = f'{item_search} is set to always ramdomize Questions'
                else:
                    result_isRandomizationOfQuestionsRequired = f'{item_search} is not set to always ramdomize Questions'
                
                APIEncapsulamento = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{itemID}/questions/'''
                
                await page.goto(url=APIEncapsulamento, wait_until='commit')
                config = 'id'
                await page.evaluate(filteredRequest_title(item_search=item_Search, config=config))
                
                return
        except Exception as e:
                if f'{item_search} not found in room {id_interno}' in str(e):
                    
                    config = 'id'
                    item_folder = f'Atividade - {item}'
                    activity_folderID = await page.evaluate(filteredRequest_title(item_search=item_folder, config=config))
                    
                    await page.goto(url=APIFolder_noPublic(activity_folderID), wait_until='commit')
                    
                    config = 'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfAnswersRequired'
                    print(f'Checking {item_search} Randomization of Answers Required...')
                    result_isRandomizationOfAnswersRequired = await page.evaluate(filteredRequest_title(item_search, config))
                    
                    if result_isRandomizationOfAnswersRequired == "ALWAYS":
                        result_isRandomizationOfAnswersRequired = f'{item_search} is set to always ramdomize Answers'
                    else:
                        result_isRandomizationOfAnswersRequired = f'{item_search} is not set to always ramdomize Answers'
                    
                    config = 'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.isRandomizationOfQuestionsRequired'
                    print(f'Checking {item_search} Randomization of Answers Required...')
                    result_isRandomizationOfQuestionsRequired = await page.evaluate(filteredRequest_title(item_search, config))
                    
                    if result_isRandomizationOfQuestionsRequired is True:
                        result_isRandomizationOfQuestionsRequired = f'{item_search} is set to always ramdomize Questions'
                    else:
                        result_isRandomizationOfQuestionsRequired = f'{item_search} is not set to always ramdomize Questions'
                    
                    config = 'contentDetail["resource/x-bb-asmt-test-link"].test.assessment.id'
                    itemID = await page.evaluate(filteredRequest_title(item_search=item_Search, config=config))
                    
                    APIEncapsulamento = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{itemID}/questions/'''
                
                    await page.goto(url=APIEncapsulamento, wait_until='commit')
                    
                    config = 'id'
                    IDcover = await page.evaluate(request_unfiltered0(config=config))
                    
                    APIBQItem = f'''{baseURL}learn/api/v1/courses/{id_interno}/assessments/{itemID}/questions/{IDcover}/questions?expand=sourceInfo'''
                    
                    await page.goto(url=APIBQItem, wait_until='commit')
                    
                    config = 'sourceInfo.name'
                    BQ_associated = await page.evaluate(request_unfiltered0(config=config))
                    
                    result = f'{item_Search} : | visibility: {result_visibility}| visibility in Gradebook : {result_visibleInBook}| Grade Model: {result_aggregationModel}| hand in date: {result_dueDate}| Attempts: {result_attempts}| possible note: {result_possible_note}| Randomization Of Answers: {result_isRandomizationOfAnswersRequired}| Randomization Of Questions: {result_isRandomizationOfQuestionsRequired}| Associated BQ: {BQ_associated}'
                    return result
                else:
                    print('Erro ao processar request:', e)
                    return
        return result

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

            if result2 != 'https://lti-kyryon.andrios.tech/v1/lti/launch':
                text = f'This link for {item_Search} is wrong: '
                result2 = f'{text}{result2}'

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

            if result2 != 'https://sofialti.ldmedtech.com.br/v1/launch/ser-sofia-plano-estudos':
                text = f'This link for {item_Search} is wrong: '
                result2 = f'{text}{result2}'

            results = f'{item_Search}: visibility: {result} | URL: {result2}'
            return results
        case 'Fale com o Tutor':
            await page.goto(url=internalID_API, wait_until='networkidle')

            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result_visibility = await page.evaluate(filteredRequest_title(item_Search, config))
            
            await page.goto(url=internalID_API_noPublic, wait_until='commit')

            config = 'contentDetail["resource/x-bb-journallink"].blog.entryModificationAllowed'
            print(f'Checking {item_Search} entryModificationAllowed...')
            result_entry_modifucation = await page.evaluate(filteredRequest_title(item_Search, config))

            config = 'contentDetail["resource/x-bb-journallink"].blog.commentModificationAllowed'
            print(f'Checking {item_Search} commentModificationAllowed...')
            result_comment_Modification = await page.evaluate(filteredRequest_title(item_Search, config))

            result = f'{item_Search}: visibility : {result_visibility} | entryModificationAllowed:'\
            f'{result_entry_modifucation} | commentModificationAllowed: {result_comment_Modification}'
            return result
        case 'Desafio Colaborativo':
            await page.goto(url=internalID_API, wait_until='networkidle')

            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))

            config = 'contentHandler.targetId'
            print(f'Checking {item_Search} contentHandler.targetId...')
            targetID = await page.evaluate(filteredRequest_title(item_Search, config))
             
            APITargetID = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{targetID}'
            await page.goto(url=APITargetID, wait_until='commit')
            
            config = 'contentHandler.discussionId'
            print(f'Checking {item_Search} contentHandler.discussionId...')
            discussionID = await page.evaluate(request_unfiltered_noResults(config=config))
            
            API_Discussion_groups = f'{baseURL}learn/api/public/v1/courses/{id_interno}/discussions/{discussionID}/groups'
            await page.goto(url=API_Discussion_groups, wait_until='commit')
            
            config = 'length'
            print(f'Checking {item_Search} groups length...')
            try:
                Groups_length = await page.evaluate(request_unfiltered(config=config))
            except Exception as e:
                Groups_length = 0
            
            if Groups_length > 0:
                text = f'{Groups_length} Groups associated'
                result = f'{result} | {text}'
            else:
                text = 'No group associated'
                result = f'{result} | {text}'
                return

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
            result = await check_item_in_all_folders_unidade(item_Search)

            return result
        case 'Videoteca: Videoaula':
            result = await check_item_in_all_folders_unidade(item_Search)

            return result
        case 'Biblioteca Virtual: e-Book':
            result = await check_item_in_all_folders_unidade(item_Search)

            return result
        case 'WebAula':
            await page.goto(url=internalID_API, wait_until='networkidle')

            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))

            config = 'id'
            print(f'Checking {item_Search} id...')
            father_id = await page.evaluate(filteredRequest_title(item_Search, config))

            await page.goto(url=APIFolder(father_id), wait_until='commit')

            config = 'length'
            result2 = await page.evaluate(request_unfiltered_toString(config=config))

            result = f'{result} | {result2} itens in {item_Search}'

            return result
        case 'Avaliações':#
            await page.goto(url=internalID_API, wait_until='networkidle')

            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))

            config = 'id'
            print(f'Checking {item_Search} id...')
            father_id = await page.evaluate(filteredRequest_title(item_Search, config))

            await page.goto(url=APIFolder(father_id), wait_until='commit')

            config = 'title'
            item_search = 'Regras da Avaliação - Resolução CONSU'
            print(f'Checking {item_search} title...')
            try:
                result2 = await page.evaluate(filteredRequest_title(item_search, config))
                result = f'{result} | {item_search} is correct!'
            except Exception as e:
                text = f'{item_search} title is incorrect!'
                result = f'{result} | {text}'

            return result
        case 'Atividade Contextualizada': #
            await page.goto(url=internalID_API, wait_until='networkidle')

            config = 'hasChildren'
            print(f'Checking {item_Search} hasChildren...')
            result_hasChidren = await page.evaluate(filteredRequest_title(item_Search, config))
            
            match result_hasChidren:
                case 'true':
                    
                    config = 'availability.available'
                    print(f'Checking {item_Search} visibility...')
                    result = await page.evaluate(filteredRequest_title(item_Search, config))
                    
                    config = 'id'
                    folderID = await page.evaluate(filteredRequest_title(item_search=item, config=config))
                    
                    await page.goto(url=APIFolder(father_id=folderID), wait_until='commit')
                    
                    await page.goto(url=APIGradeCollum, wait_until='commit')
                    
                    # contentHandler.assessmentId
                    
                    return result
                case 'false':
                    
                    # verificar configs e conteúdo
                    config = 'availability.available'
                    print(f'Checking {item_Search} visibility...')
                    result = await page.evaluate(filteredRequest_title(item_Search, config))
                    
                    return result
            # verificar se tem conteúdo na atividade
            
            return result
        case 'AV1': #
            await page.goto(url=APIGradeCollum, wait_until='commit')

            config = 'genericReadOnlyData.dueDate'
            print(f'Checking {item_Search} hand in date...')
            result = await page.evaluate(filteredRequest_columnName(item_Search, config))
            # verificar se é uma pasta, um cálculo ou um item
            # other configs

            return result
        case 'AV2': #
            await page.goto(url=APIGradeCollum, wait_until='commit')

            result = await page.evaluate(filteredRequest_columnName(item_Search, config))

            # other configs

            return result
        case 'AF': #
            await page.goto(url=APIGradeCollum, wait_until='commit')

            result = await page.evaluate(filteredRequest_columnName(item_Search, config))

            # configs valor da note, nomeclatura certa, se está visivel para o aluno

            return result
        case 'SER Melhor (Clique Aqui para deixar seu elogio, crítica ou sugestão)':
            await page.goto(url=internalID_API, wait_until='networkidle')

            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))

            config = 'contentHandler.url'
            print(f'Checking {item_Search} associated URL...')
            result2 = await page.evaluate(filteredRequest_title(item_Search, config))

            # Verificar se o link está correto

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

            # Verificar se o link está correto

            results = f'{item_Search}: visibility: {result} | URL: {result2}'
            return results
        case 'Relatório de Aulas Práticas': #
            await page.goto(url=internalID_API, wait_until='networkidle')

            item = 'Atividade de Aulas Práticas'
            config = 'id'
            folderID = await page.evaluate(filteredRequest_title(item_search=item, config=config))
            
            await page.goto(url=APIFolder(father_id=folderID), wait_until='commit')
            #verify other itens in folder
            
            await page.goto(url=APIGradeCollum, wait_until='commit')

            return result
        case 'Atividade de Autoaprendizagem 1':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'
            
            return result
        case 'Atividade de Autoaprendizagem 2':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'
            
            return result
        case 'Atividade de Autoaprendizagem 3':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'
            
            return result
        case 'Atividade de Autoaprendizagem 4':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'

            return result
        case 'Avaliação On-Line 1 (AOL 1) - Questionário':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'

            return result
        case 'Avaliação On-Line 2 (AOL 2) - Questionário':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'

            return result
        case 'Avaliação On-Line 3 (AOL 3) - Questionário':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'

            return result
        case 'Avaliação On-Line 4 (AOL 4) - Questionário':
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'
            
            return result
        case 'Avaliação On-Line 5 (AOL 5) - Atividade Contextualizada': #
            result_configs = await activity_configs(item_Search)
            
            result = f'{result_configs}'

            return result
        case _:
            result = f'Item: [{item_Search}] não encontrado ou nomeclatura errada'
            print(result)
            return result

async def adjust_date(utc_time_str: str):
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

async def doublecheck_config_main_test() -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        
        CACHE_FILE = r'src\Metodos\Login\__pycache__\login_cache.json'
        with open(CACHE_FILE, 'r') as f:
            cache_data = json.load(f)
            await page.context.add_cookies(cache_data['cookies'])

        baseURL = 'https://sereduc.blackboard.com/'
        id_interno = '_187869_1' # sala carlos
        # id_interno = '_139625_1' #sala modelo
        
        await page.goto(url=baseURL, wait_until='commit')
        
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Fórum de Interação entre Professores e Tutores')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Meu Desempenho')
        result03 =await API_Config(page=page, id_interno=id_interno, item_Search='Organize seus estudos com a Sofia')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Fale com o Tutor')
        result02 =await API_Config(page=page, id_interno=id_interno, item_Search='Desafio Colaborativo')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Unidade 1')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Unidade 2')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Unidade 3')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Unidade 4')
        result0 = await API_Config(page=page, id_interno=id_interno, item_Search='Material Didático Interativo')
        result1 = await API_Config(page=page, id_interno=id_interno, item_Search='Videoteca: Videoaula')
        result2 = await API_Config(page=page, id_interno=id_interno, item_Search='Biblioteca Virtual: e-Book')
        results04 = await API_Config(page=page, id_interno=id_interno, item_Search='Atividade de Autoaprendizagem 1')
        results04 = await API_Config(page=page, id_interno=id_interno, item_Search='Atividade de Autoaprendizagem 2')
        results04 = await API_Config(page=page, id_interno=id_interno, item_Search='Atividade de Autoaprendizagem 3')
        results04 = await API_Config(page=page, id_interno=id_interno, item_Search='Atividade de Autoaprendizagem 4')
        results05 = await API_Config(page=page, id_interno=id_interno, item_Search='Avaliação On-Line 1 (AOL 1) - Questionário')
        results05 = await API_Config(page=page, id_interno=id_interno, item_Search='Avaliação On-Line 2 (AOL 2) - Questionário')
        results05 = await API_Config(page=page, id_interno=id_interno, item_Search='Avaliação On-Line 3 (AOL 3) - Questionário')
        results05 = await API_Config(page=page, id_interno=id_interno, item_Search='Avaliação On-Line 4 (AOL 4) - Questionário')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Avaliações')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='WebAula')
        results00 = await API_Config(page=page, id_interno=id_interno, item_Search='Solicite seu livro impresso')
        results01 = await API_Config(page=page, id_interno=id_interno, item_Search='SER Melhor (Clique Aqui para deixar seu elogio, crítica ou sugestão)')
        # result =f'\n{result0}\n{result1}\n{result2}\n{result02}\n{results00}\n{results01}\n{result02}\n{result03}\n{results04}\n{results05}'
        # result_test = '\n*{}\n'.format(result)
        # print('{:5} | {}'.format(f'Run: {index}',executionTime))
        # print(result_test)

if __name__ == "__main__":
    asyncio.run(doublecheck_config_main_test())