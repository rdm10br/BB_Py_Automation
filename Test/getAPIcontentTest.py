import asyncio, json, typing, pytz
from datetime import datetime
from playwright.async_api import (async_playwright, expect, Page)


async def API_Config(page: Page, id_interno: str, item_Search: str) -> str:
    
    baseURL = 'https://sereduc.blackboard.com/'
    internalID_API = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents'''
    APIGradeCollum = f'''{baseURL}learn/api/v1/courses/{id_interno}/gradebook/columns'''
    
    
    def APIFolder(father_id: str):
        API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children'
        return API
    
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
    
    def filteredRequest_title(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.title === "{item_search}");
            if (data && data.{config}) {{
                return data.{config};
            }} else {{
                throw new Error('{item_search} not found in room {id_interno}');
                }}
            }}'''
        return request

    def filteredRequest_name(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.name === "{item_search}");
            if (data && data.{config}) {{
                return data.{config};
            }} else {{
                throw new Error('{item_search} not found in room {id_interno}');
                }}
            }}'''
        return request

    def filteredRequest_columnName(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.columnName === "{item_search}");
            if (data && data.{config}) {{
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
            print(f'Checking {item_search} visibility...')
            
            try:
                result_visibility = await page.evaluate(filteredRequest_title(item_search, config))
            except Exception as e:
                if f'{item_search} not found in room {id_interno}' in str(e):
                    print(f'Erro na sala: {id_interno}; Item: {item_Search} não foi encontrado')
                    continue
                else:
                    print('Erro ao processar request:', e)
                    continue
            
            config = 'contentHandler.url'
            print(f'Checking {item_search} associated URL...')
            
            try:
                result_url = await page.evaluate(filteredRequest_title(item_search, config))
            except Exception as e:
                if f'{item_search} not found in room {id_interno}' in str(e):
                    print(f'Erro na sala: {id_interno}; Item: {item_Search} não foi encontrado')
                    continue
                else:
                    print('Erro ao processar request:', e)
                    continue
            
            #verificar validade do link
            
            if result_visibility != f'{item_search} not found in room {id_interno}':
                results = f'{results}{item_Search} from Unidade {i} : visibility: {result_visibility} | URL: {result_url}\n'
            else:
                results = f'{results}{item_search} não encontrado na Unidade {i}\n'
        
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
            
            if result2 != 'lti-kyryon.andrios.tech/v1/lti/launch':
                text =f'This link for {item_Search} is wrong: '
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
            
            if result2 !='sofialti.ldmedtech.com.br/v1/launch/ser-sofia-plano-estudos':
                text =f'This link for {item_Search} is wrong: '
                result2 = f'{text}{result2}'
            #Verificar se o link está correto
            
            results = f'{item_Search}: visibility: {result} | URL: {result2}'
            return results
        
        case 'Fale com o Tutor':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result_visibility = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentDetail["resource/x-bb-journallink"].blog.entryModificationAllowed'
            print(f'Checking {item_Search} entryModificationAllowed...')
            result_entry_modifucation = await page.evaluate(filteredRequest_title(item_Search, config))
            
            config = 'contentDetail["resource/x-bb-journallink"].blog.commentModificationAllowed'
            print(f'Checking {item_Search} commentModificationAllowed...')
            result_comment_Modification = await page.evaluate(filteredRequest_title(item_Search, config))
            
            result = f'{item_Search}: visibility : {result_visibility} | entryModificationAllowed: {result_entry_modifucation} | commentModificationAllowed: {result_comment_Modification}'
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
            
            result = await check_item_in_all_folders_unidade(item_Search)
            
            return result
        
        case 'Videoteca: Videoaulas':
            
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
            
            config = 'lenght'
            result2 = await page.evaluate(request_unfiltered(config=config))
            
            result = f'{result} | {result2} itens in {item_Search}'
            
            return result
        
        case 'Avaliações':
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
            result2 = await page.evaluate(filteredRequest_title(item_search, config))
            
            if result2 != 'Regras da Avaliação - Resolução CONSU':
                text = f'{item_search} title is incorrect!'
                result = f'{result}{text}'
            else:
                result = f'{result} | {item_search} is correct!'
            
            return result
        
        case 'Atividade Contextualizada':
            await page.goto(url=internalID_API, wait_until='networkidle')
            
            config = 'availability.available'
            print(f'Checking {item_Search} visibility...')
            result = await page.evaluate(filteredRequest_title(item_Search, config))
            # verificar se tem conteúdo na atividade
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
        # result0 = await API_Config(page=page, id_interno=id_interno, item_Search='Material Didático Interativo')
        # result1 = await API_Config(page=page, id_interno=id_interno, item_Search='Videoteca: Videoaulas')
        # result2 = await API_Config(page=page, id_interno=id_interno, item_Search='Biblioteca Virtual: e-Book')
        await page.wait_for_timeout(5*1000)
        # print(visibility, item_URL)
        # print(result0)
        # print(result1)
        # print(result2)


if __name__ == "__main__":
    asyncio.run(main())