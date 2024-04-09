import regex as re
from playwright.async_api import Playwright, async_playwright, expect, Page


from Metodos.API import getPlanilha
# import getPlanilha

async def API_Req(page: Page, index) -> None:
    
    id_externo = getPlanilha.getCell(index=index)
    
    baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'
    
    await page.goto(internalID_API)
    id_interno = await page.evaluate('() => {return JSON.parse(document.body.innerText).id}')
    return str(id_interno)
    
async def API_Ativ_Course(page: Page, id_externo) -> None:
    
    baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'
    
    request = '() => {return JSON.parse(document.body.innerText).name.match(/(?<=[(]).*(?=[)])/)}'
    
    await page.goto(internalID_API)
    course_area = await page.evaluate(request)
    # Remover caracteres especiais usando expressões regulares
    string_sem_especiais = re.sub(r'[^\w\s]', '', str(course_area))
    return str(course_area)