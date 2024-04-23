import asyncio, gc, pytest, docx
from playwright.async_api import Playwright, async_playwright, expect


#importando Metodos principais
from Metodos import checkup_login, getFromAPI, getBQ, fileChooser


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    
    baseURL = 'https://sereduc.blackboard.com/'
    classURL = f'{baseURL}ultra/courses/'
    id_repository = '_187869_1'
    
    rootBQ = f'{baseURL}webapps/assessment/do/authoring/'\
    f'viewAssessmentManager?assessmentType=Pool&course_id={id_repository}'
    
    id_BQ = '_24977260_1'
    
    rootBQTest = (f'{baseURL}webapps/assessment/do/authoring/'\
    'modifyAssessment?method=modifyAssessment&'\
    'copyAlignments=false&packageFormat=undefined&'\
    f'course_id={id_repository}'\
    f'&assessmentId={id_BQ}&sectionId=&questionId=&saveAsNew=false&'\
    'questionIsNew=false&createAnother=false&assessmentType=Pool&'\
    'isLinkedQuestion=&'\
    'referencingQuestionId=')
    
    await checkup_login.checkup_login(page=page)
    
    cookies = await page.context.cookies(urls=baseURL)
    
    path = fileChooser.window_file()
    # path = r'C:\Users\013190873\Downloads\teste.docx'
    doc = len(docx.Document(docx=path).paragraphs)
    print(doc)
    
    for index in range(doc):
        index +=1
        
        new_browser = await playwright.chromium.launch(headless=False)
        new_context = await new_browser.new_context(no_viewport=True)
        await new_context.add_cookies(cookies)
        new_page = await new_context.new_page()
        print(index)
        await new_page.goto(rootBQTest)
        await new_page.wait_for_timeout(1000)
        
        await new_context.close()
        await new_browser.close()
        
        gc.collect()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())