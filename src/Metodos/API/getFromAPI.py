import regex as re
from playwright.async_api import Page
from functools import lru_cache


from Metodos.API import getPlanilha
# import getPlanilha

async def API_Req(page: Page, index: int) -> str:
    """
    Async Function that search in the API for the internal_ID of the classroom
    you want, in the order of the Excel file you gave.
    

    Args:
        page (Page): Page constructor form Playwright that
        you want this API to run
        index (int): the index of line in the excel file, and tha times
        it looped

    Returns:
        str: ```internal_ID```
    """
    id_externo = getPlanilha.getCell(index=index)
    
    # baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'./learn/api/public/v3/courses/courseId:{id_externo}'

    print(f'Looking on Api Request to find internal ID of {id_externo}')

    await page.goto(internalID_API)
    id_interno = await page.evaluate('() => {return JSON.parse(document.body.innerText).id}')
    return str(id_interno)
    
async def API_Ativ_Course(page: Page, id_externo: str) -> str:
    """
    Async Function that search in the API for the ```course_area``` of the
    classroom you want, in the order of the Excel file you gave.

    Args:
        page (Page): Page constructor form Playwright that
        you want this API to run
        id_externo (str): the External ID of the classroom you want

    Returns:
        str: ```course_area```
    """
    # baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'./learn/api/public/v3/courses/courseId:{id_externo}'
    
    request = '() => {return JSON.parse(document.body.innerText).name.match(/(?<=[(]).*(?=[)])/)}'

    print(f'Looking on Api Request Activity to find course area of {id_externo}')

    await page.goto(internalID_API)
    course_area = await page.evaluate(request)
    # Remover caracteres especiais usando expressões regulares
    string_sem_especiais = re.sub(r'[^\w\s]', '', str(course_area))
    return str(course_area)

@lru_cache
async def API_Ativ_Groups(page: Page, id_interno: str, item: str) -> str:
    """_summary_

    Args:
        page (Page): _description_
        id_interno (str): _description_
        item (str): Group Name

    Returns:
        str: Group ID
    """
    url = f'./learn/api/public/v1/courses/{id_interno}/groups/'
    config = 'id'
    request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.name === "{item}");
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('Group: {item} not found in room {id_interno}');
                }}
            }}'''
            
    await page.goto(url)
    id_group = await page.evaluate(request)
    return id_group

async def API_AP_Rules(page: Page, id_interno: str, id_item: str) -> str:
    
    url_rules = f'./learn/api/public/v1/courses/{id_interno}/contents/{id_item}/adaptiveRelease/rules/'
    
    def url_criteria(id_rule: str):
        return (f'./learn/api/public/v1/courses/{id_interno}/contents/{id_item}/adaptiveRelease/rules/{id_rule}/criteria/')
    
    def url_final(id_rule: str, id_criteria: str):
        return (f'./learn/api/public/v1/courses/{id_interno}/contents/{id_item}/adaptiveRelease/rules/{id_rule}/criteria/{id_criteria}/groups')
    
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
    
    def request_type(item: str, _config: str):
        return (f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.type === "{item}");
            if (data && (data.{_config}).toString) {{
                return data.{_config};
            }} else {{
                throw new Error('Group: {item} not found in room {id_interno}');
                }}
            }}''')
    
    await page.goto(url_rules)
    id_rule = await page.evaluate(request_unfiltered0(config='id'))
    
    await page.goto(url_criteria(id_rule))
    id_criteria = await page.evaluate(request_type(item='Memberships', _config='id'))
    
    await page.goto(url_final(id_rule, id_criteria))
    id_group = await page.evaluate(request_unfiltered0(config='groupId'))
    
    return id_group

@lru_cache
async def check_item_in_all_folders_unidade(page: Page, id_interno: str, item_search: str):
    results = ''
    id_folder: list = []
    internalID_API = f''
    
    def filteredRequest_title(item: str, _config: str):
        return (f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.title === "{item}");
            if (data && (data.{_config}).toString) {{
                return data.{_config};
            }} else {{
                throw new Error('Group: {item} not found in room {id_interno}');
                }}
            }}''')
    
    def APIFolder(father_id: str):
        API = f'./learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children'
        return API
    
    try:
        await page.goto(url=internalID_API, wait_until='networkidle')

        for index in range(2):
            index += 1
            config = 'id'
            unidade = f'AV{index} - Atividade Prática de Extensão'
            print(f'Checking AV{index} - Atividade Prática de Extensão id...')
            id_value = await page.evaluate(filteredRequest_title(item_search=unidade, config=config))
            id_folder.append(id_value)
            print(id_folder[index-1])

        for i in range(2):
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
                    result = f'{result}\nErro na sala: {id_interno}; Item: {item_search} não foi encontrado'
                    print(f'Erro na sala: {id_interno}; Item: {item_search} não foi encontrado')
                    continue
                else:
                    print('Erro ao processar request:', e)
                    continue
                
            new_result = f'''{item_search} from Unidade {i} :
            visibility: {result_visibility} |
            URL: {result_url}\n'''
            if result_visibility != f'{item_search} not found in room {id_interno}':
                results = f'''{results}{new_result}'''
            else:
                results = f'{results}{item_search} não encontrado na Unidade {i}\n'
            
            item = f'{item_search} from Unidade {i}'
        return results
    except:
        print('folder or item not found')