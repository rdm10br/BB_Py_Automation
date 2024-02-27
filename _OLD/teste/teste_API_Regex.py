from playwright.sync_api import Playwright, sync_playwright, expect
import re

def API_Ativ_Course(playwright: Playwright ,id_externo) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    
    baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'{baseURL}learn/api/public/v3/courses/courseId:{id_externo}'
    
    request = '() => {return JSON.parse(document.body.innerText).name.match(/(?<=[(]).*(?=[)])/)}'
    
    page.goto(internalID_API)
    teste = page.evaluate(request)
    # Remover caracteres especiais usando expressões regulares
    string_sem_especiais = re.sub(r'[^\w\s]', '', str(teste))
    page.close()
    return str(string_sem_especiais)
    
# with sync_playwright() as playwright:
#     id_externo = '7.8225.216597'
#     id1=API_Req(playwright,id_externo)
#     print(id1)