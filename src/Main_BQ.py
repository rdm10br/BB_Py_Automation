import asyncio, gc, sys
from playwright.async_api import Playwright, async_playwright, expect
from functools import lru_cache


#importando Metodos principais
from Metodos import checkup_login, getFromAPI, getBQ, fileChooser, create_bq
from Decorators import capture_console_output_async, TimeStampedStream

@lru_cache
@capture_console_output_async
async def run(playwright: Playwright) -> None:
    sys.stdout = TimeStampedStream(sys.stdout)
    browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    
    baseURL = 'https://sereduc.blackboard.com/'
    classURL = f'{baseURL}ultra/courses/'
    id_repository = '_187869_1'
    bq_id = f'{baseURL}learn/api/v1/courses/{id_repository}/assessments/'
    rootBQ = f'{baseURL}webapps/assessment/do/authoring/'\
    f'viewAssessmentManager?assessmentType=Pool&course_id={id_repository}'
    
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
    
    await checkup_login.checkup_login(page=page)
    
    cookies = await page.context.cookies(urls=baseURL)
    
    path = fileChooser.window_file()
    doc = getBQ.enunciado_count(path=path)
    print(doc)
    
    await page.goto(rootBQ)
    BQ_name = await create_bq.create_bq(page=page, path=path)
    await page.goto(bq_id)
    id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
    await page.goto(BQTest(id_BQ=id_BQ))
    
    for index in range(doc):
        index +=1
        
        new_context = await browser.new_context(no_viewport=True)
        await new_context.add_cookies(cookies)
        new_page = await new_context.new_page()
        
        print(f'\nQuestão : {index}')
        
        await new_page.goto(BQTest)
        await new_page.wait_for_timeout(1000)
        
        await create_bq.create_question(index=index, path=path, page=new_page)
        
        await new_context.close()
        
        gc.collect()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())