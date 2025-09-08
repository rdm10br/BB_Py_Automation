import regex as re
from playwright.sync_api import Page

async def adjust_name(page: Page, id_interno: str, name: str = 'Dce') -> None:
    
    # API Mescla
    API_M = f'./learn/api/public/v3/courses/{id_interno}'
    
    # API Courses
    API_C = f'./learn/api/public/v1/courses/{id_interno}/children?expand=childCourse'
    
    def SearchOnBlack(id_externo): return f'./webapps/blackboard/execute/courseManager?sourceType=COURSES&courseInfoSearchKeyString=CourseId&courseInfoSearchOperatorString=Equals&courseInfoSearchText={id_externo}'
    
    request_length = 'JSON.parse(document.body.innerText).results.length'
    
    def transform_text(text: str):
        # Check if 'Dce' already exists in the text
        
        if 'Dce Uninorte - Dce' in text and name != 'Dce Uninorte - Dce':
            print(f'{text} changing...')
            text = text.replace('Dce Uninorte - Dce - ', f'{name} - ')
            print(f' to {text}')
            return text
        elif 'Dce Uninorte' in text and name != 'Dce Uninorte':
            print(f'{text} changing...')
            text = text.replace('Dce Uninorte - ', f'{name} - ')
            print(f' to {text}')
            return text
        elif 'Dce' in text and name != 'Dce':
            print(f'[DCE]{text} changing...')
            text = text.replace('Dce - ', f'{name} - ')
            print(f' to {text}')
            return text
        elif name in text:
            print(f'{text} already contains {name}. No change needed.')
            return text

            
        # Use regex to insert 'Dce - ' after the numeric code pattern
        print(f'{text} changing...')
        transformed_text = re.sub(r"(\d+ \.\s\d+ - )", fr"\1{name} - ", text)
        print(f' to {transformed_text}')
        return transformed_text
    
    def request(_config: str, i: int) -> str:
        req = f'''() => {{
            const data = JSON.parse(document.body.innerText).results[{i}];
            if (data && String(data.{_config})) {{
                return data.{_config};
            }} else {{
                throw new Error('Not found in room {id_interno}');
                }}
            }}'''
        return req
    
    def request_no_result(_config: str) -> str:
        req = f'''() => {{
            const data = JSON.parse(document.body.innerText);
            if (data && String(data.{_config})) {{
                return data.{_config};
            }} else {{
                throw new Error('Not found in room {id_interno}');
                }}
            }}'''
        return req
    
    configs = [
        'name',
        'externalId',
        'hasChildren'
    ]
    configs_children = [
        'childCourse.name',
        'childCourse.externalId'
    ]
    
    results = {}
    
    if id_interno not in results:
        results[id_interno] = {}
    
    await page.goto(API_M, wait_until='domcontentloaded')
    
    for config in configs:
        result = await page.evaluate(request_no_result(config))
        
        if config == 'name':
            text = result
            result = transform_text(result)
        
        # if config == 'name' and result == text:
        #     print(f'No change needed for main course name: {result}')
        # else:
        results[id_interno][config] = result
        
    if str(results[id_interno]['hasChildren']).lower() == 'true':
        
        await page.goto(API_C, wait_until='domcontentloaded')
        
        length = await page.evaluate(request_length)
        
        print(f'{id_interno} : {length} courses')
        
        for i in range(length):
            if i not in results[id_interno]:
                results[id_interno][i] = {}
            for config in configs_children:
                result = await page.evaluate(request(config, i))
                
                if config == 'childCourse.name':
                    result = transform_text(result)
                
                results[id_interno][i][config] = result
                       
        await page.goto(SearchOnBlack(results[id_interno]['externalId']), wait_until='domcontentloaded')
        
        await page.get_by_role("link", name=results[id_interno]['externalId']).click()
        await page.wait_for_load_state('domcontentloaded')
        
        await page.get_by_label("Editar o nome do curso").click()
        await page.get_by_role("textbox").press("ControlOrMeta+a")
        await page.get_by_role("textbox").fill(results[id_interno]['name'])
        await page.get_by_role("textbox").press("Enter")
        
        for i in range(length):
            await page.goto(SearchOnBlack(results[id_interno]['externalId']), wait_until='domcontentloaded')
            
            await page.get_by_role("link", name=results[id_interno][i]['childCourse.externalId']).click()
            await page.wait_for_load_state('domcontentloaded')
            
            await page.get_by_label("Editar o nome do curso").click()
            await page.get_by_role("textbox").press("ControlOrMeta+a")
            await page.get_by_role("textbox").fill(results[id_interno][i]['childCourse.name'])
            await page.get_by_role("textbox").press("Enter")