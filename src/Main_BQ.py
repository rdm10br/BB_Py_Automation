import asyncio, gc, sys, time
from playwright.async_api import Playwright, async_playwright, expect
from functools import lru_cache


#importando Metodos principais
from Metodos import checkup_login, getFromAPI, getBQ, fileChooser, create_bq
from Decorators import capture_console_output_async, TimeStampedStream

@lru_cache
@capture_console_output_async
async def run(playwright: Playwright) -> None:
    sys.stdout = TimeStampedStream(sys.stdout)
    print('\nExecution Start')
    
    browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'], timeout=60*1000)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    
    baseURL = 'https://sereduc.blackboard.com/'
    # classURL = f'{baseURL}ultra/courses/'
    id_repository = '_247460_1'
    
    rootBQ = f'{baseURL}webapps/assessment/do/authoring/'\
    f'viewAssessmentManager?assessmentType=Pool&course_id={id_repository}'
    
    limit = 10
    offset = 0
    maxLimit = 2147483647
    
    bq_id = f'{baseURL}learn/api/v1/courses/{id_repository}/assessments?limit={limit}&offset={offset}'
    
    def API_bq_id(_offset: int):
        API = f'{baseURL}learn/api/v1/courses/{id_repository}/assessments?limit={limit}&offset={_offset}'
        return API
    
    def BQTest(id_BQ: str):
        BQ = f'{baseURL}webapps/assessment/do/authoring/modifyAssessment?'\
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
    
    await page.goto(rootBQ)
    BQ_name = await create_bq.create_bq(page=page, path=path)
    print(BQ_name)
    await page.goto(bq_id)
    
    id_BQ = ''
    while not id_BQ:
        try:
            id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
        except Exception as e:
            print(f'Error fetching id_BQ: {e}')
            try:
                offset+=limit
                id_BQ = await loop_BQ_id(offset)
            except Exception as e:
                print(f'Error in loop_BQ_id: {e}')


    await page.goto(BQTest(id_BQ=id_BQ))
    
    for index in range(doc):
        index +=1
        
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