from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
import getPlanilha

def API_Req(playwright: Playwright  ,index) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    
    id_externo = getPlanilha.getCell(index)
    
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