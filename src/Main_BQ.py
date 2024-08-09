import asyncio, gc, sys, time, os
from playwright.async_api import Playwright, async_playwright, expect
from functools import lru_cache
import regex as re
from unidecode import unidecode
from dotenv import load_dotenv


#importando Metodos principais
from Metodos import checkup_login, getBQ, fileChooser, create_bq, junctionWindow
from Decorators import capture_console_output_async, TimeStampedStream

@lru_cache
@capture_console_output_async
async def run(playwright: Playwright) -> None:
    load_dotenv()
    id_repository = os.getenv('ID_REPOSITORY')
    baseURL = os.getenv('BASE_URL')
    
    sys.stdout = TimeStampedStream(sys.stdout)
    print('\nExecution Start')
    
    browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'], timeout=60*1000)
    context = await browser.new_context(base_url=baseURL, no_viewport=True)
    page = await context.new_page()
    
    
    rootBQ = f'./webapps/assessment/do/authoring/'\
    f'viewAssessmentManager?assessmentType=Pool&course_id={id_repository}'
    
    limit = 100
    offset = 0
    maxLimit = 2147483647 # 2_147_483_647
    
    bq_id = f'./learn/api/v1/courses/{id_repository}/assessments?limit={limit}&offset={offset}'
    bq_id_max = f'./learn/api/v1/courses/{id_repository}/assessments?limit={maxLimit}&offset={offset}'
    
    def API_bq_id(_offset: int):
        API = f'./learn/api/v1/courses/{id_repository}/assessments?limit={limit}&offset={_offset}'
        return API
    
    def BQTest(id_BQ: str):
        BQ = f'./webapps/assessment/do/authoring/modifyAssessment?'\
            f'method=modifyAssessment&course_id={id_repository}'\
            f'&assessmentId={id_BQ}'
        return BQ
    
    def filteredRequest_title(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.title === "{item_search}");
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('{item_search} not found in room {id_repository}');
                }}
            }}'''
        return request
    
    async def loop_BQ_id(Offset: int):
        await page.goto(API_bq_id(_offset=Offset))
        id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
        return id_BQ
    
    start_time0 = time.time()
    await checkup_login.checkup_login(page=page)
    end_time0 = time.time()
    execution_time = end_time0 - start_time0
    executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
    print(executionTime0)
    
    cookies = await page.context.cookies(urls=baseURL)
    print('cookies caught')
    
    path = fileChooser.window_file()
    
    print('files caught')
    doc = getBQ.enunciado_count(path=path)
    print(doc)
    
    file_name = os.path.basename(path)
    BQ_name = re.sub(r'.docx','',file_name).upper()
    unidade = ''.join([ch for ch in BQ_name if ch.isdigit()])
    match unidade[0]:
            case '1' :
                item = 'BQ 01'
            case '2' :
                item = 'BQ 02'
            case '3' :
                item = 'BQ 03'
            case '4' :
                item = 'BQ 04'
    BQ_name = unidecode(BQ_name)
    BQ_name = re.sub(r'\d','',BQ_name)
    BQ_name = re.sub(r'\s+', ' ', BQ_name)
    BQ_name = re.sub(r'\s$', '', BQ_name)
    BQ_name = re.sub(r'^\s', '', BQ_name)
    BQ_name = BQ_name.strip()
    BQ_name = f'{BQ_name} - {item}_GRADUACAO'
    print(BQ_name)
            
    isjunction = junctionWindow.window()
        
    try:
        id_BQ = ''
        BQ_count = 0
        await page.goto(bq_id_max)
        id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
        if isjunction == 'No':
            BQ_count = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='questionCount'))
        elif isjunction == 'Yes':
            pass
        print(f'ID found: {id_BQ}')
    except Exception as e:
        await page.goto(rootBQ)
        await create_bq.create_bq(page=page, BQ_name=BQ_name)
        await page.goto(bq_id)
        
        length = await page.evaluate('JSON.parse(document.body.innerText).results.length')
        count = await page.evaluate('JSON.parse(document.body.innerText).paging.count')
        # counter = count - length
        
        while not id_BQ:
            try:
                id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
                print(f'ID found: {id_BQ}')
            except Exception as e:
                print(f'Error fetching id_BQ: {e}')
                try:
                    if offset <= count:
                        offset+=length
                        id_BQ = await loop_BQ_id(offset)
                        print(f'ID found: {id_BQ}')
                except Exception as e:
                    print(f'Error in loop_BQ_id: {e}')


    await page.goto(BQTest(id_BQ=id_BQ))
    
    for index in range(doc):
        index +=1
        if index <= BQ_count:
            print(f'\nQuestão : {index} - already made!')
            pass
        else:
            new_context = await browser.new_context(no_viewport=True)
            await new_context.add_cookies(cookies)
            new_page = await new_context.new_page()
            
            start_time = time.time()
            print(f'\nQuestão : {index}')
            
            await new_page.goto(url=BQTest(id_BQ=id_BQ), wait_until='commit')
            # await new_page.wait_for_timeout(1000)
            
            await create_bq.create_question(index=index, path=path, page=new_page)
            
            await new_context.close()
            
            end_time = time.time()
            execution_time = end_time - start_time
            executionTime = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
            print('{:5} | {}'.format(f'Run: {index}',executionTime))
            
            gc.collect()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
        
asyncio.run(main())