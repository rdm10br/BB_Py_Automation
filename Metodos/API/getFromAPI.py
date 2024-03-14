from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
import re
from Metodos.API import getPlanilha
# import getPlanilha

def API_Req(playwright: Playwright  ,index) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    
    id_externo = getPlanilha.getCell(index=index)
    
    baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'
    
    page.goto(internalID_API)
    id_interno = page.evaluate('() => {return JSON.parse(document.body.innerText).id}')
    page.close()
    return str(id_interno)

# with sync_playwright() as playwright:
#     index=1
#     id1=API_Req(playwright,index)
#     print(id1)
    
def API_Ativ_Course(playwright: Playwright ,id_externo) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    
    baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'
    
    request = '() => {return JSON.parse(document.body.innerText).name.match(/(?<=[(]).*(?=[)])/)}'
    
    page.goto(internalID_API)
    course_area = page.evaluate(request)
    # Remover caracteres especiais usando expressões regulares
    # string_sem_especiais = re.sub(r'[^\w\s]', '', str(course_area))
    page.close()
    return str(course_area)

# with sync_playwright() as playwright:
#     id_externo = '7.8225.216597'
#     id1=API_Ativ_Course(playwright,id_externo)
#     print(id1)