import regex as re
from playwright.sync_api import Page

async def open_Mescla(page: Page, id_interno: str) -> None:
    
    # API Mescla
    API_M = f'./learn/api/public/v3/courses/{id_interno}'
    
    # API Courses
    API_C = f'./learn/api/public/v1/courses/{id_interno}/children?expand=childCourse'
    
    def SearchOnBlack(id_externo): return f'./webapps/blackboard/execute/courseManager?sourceType=COURSES&courseInfoSearchKeyString=CourseId&courseInfoSearchOperatorString=Equals&courseInfoSearchText={id_externo}'
    
    request_length = 'JSON.parse(document.body.innerText).results.length'
    
    def transform_text(text: str):
        # Check if 'Dce' already exists in the text
        if 'Dce' in text:
            return text
        
        # Use regex to insert 'Dce - ' after the numeric code pattern
        transformed_text = re.sub(r"(\d{6} \.\s\d - )", r"\1Dce - ", text)
        return transformed_text
    
    def request(_config: str, i: int) -> str:
        req = f'''() => {{
            const data = JSON.parse(document.body.innerText).results[{i}];
            if (data && (data.{_config}).toString) {{
                return data.{_config};
            }} else {{
                throw new Error('Not found in room {id_interno}');
                }}
            }}'''
        return req
    
    def request_no_result(_config: str) -> str:
        req = f'''() => {{
            const data = JSON.parse(document.body.innerText);
            if (data && (data.{_config}).toString) {{
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
    
    await page.goto(API_M, wait_until='domcontentloaded')
    
    for config in configs:
        result = await page.evaluate(request_no_result(config))
        
        if config == 'name':
            result = transform_text(result)
        
        results[id_interno][config] = result
        
    if str(results[id_interno]['hasChildren']).lower() == 'true':
        
        await page.goto(API_C, wait_until='domcontentloaded')
        
        length = await page.evaluate(request_length)
        
        for i in range(length):
            for config in configs_children:
                result = await page.evaluate(request(config, i))
                
                if config == 'childCourse.name':
                    result = transform_text(result)
                
                results[id_interno][i][config] = result
                       
        await page.goto(SearchOnBlack(results[id_interno]['externalId']))