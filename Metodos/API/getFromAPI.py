import regex as re
from playwright.async_api import Playwright, async_playwright, expect, Page


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
    
    baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'

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
    baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'
    
    request = '() => {return JSON.parse(document.body.innerText).name.match(/(?<=[(]).*(?=[)])/)}'

    print(f'Looking on Api Request Activity to find course area of {id_externo}')

    await page.goto(internalID_API)
    course_area = await page.evaluate(request)
    # Remover caracteres especiais usando expressões regulares
    string_sem_especiais = re.sub(r'[^\w\s]', '', str(course_area))
    return str(course_area)