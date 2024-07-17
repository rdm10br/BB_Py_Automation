from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *


def API_Req_Content(playwright: Playwright  , id_interno, item_Search) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents?title={item_Search}'
    
    page.goto(internalID_API)
    
    # request = '() => {return JSON.parse(document.body.innerText).results[0].id}'
    
    request = '''() => {
    const data = JSON.parse(document.body.innerText).results;
    if (data && data.length > 0 && data[0].id) {
        return data[0].id;
    } else {
        throw new Error('Item não encontrado');
    }
    }'''

    try:
        id_sofia = page.evaluate(request)
        page.close()
        # print(str(id_sofia))
        return str(id_sofia)
    except Exception as e:
        if 'Item não encontrado' in str(e):
            print(f'Erro na sala: {id_interno} no Item: {item_Search} não foi encontrado')
            return
        else:
            print('Erro ao processar request:', e)

# with sync_playwright() as playwright:
#     itemS = 'avaliações'
#     id_I = '_26709_1'
#     id1=API_Req_Content(playwright,id_I,itemS)

def API_Req_Content_children(playwright: Playwright  , id_interno, father_id, item_Search) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children?title={item_Search}'
    
    page.goto(internalID_API)
    
    # request = '() => {return JSON.parse(document.body.innerText).results[0].id}'
    
    request = '''() => {
    const data = JSON.parse(document.body.innerText).results;
    if (data && data.length > 0 && data[0].id) {
        return data[0].id;
    } else {
        throw new Error('Item não encontrado');
    }
    }'''

    try:
        id_sofia = page.evaluate(request)
        page.close()
        # print(str(id_sofia))
        return str(id_sofia)
    except Exception as e:
        if 'Item não encontrado' in str(e):
            print(f'Erro na sala: {id_interno} no Item: {item_Search} não foi encontrado')
            return
        else:
            print('Erro ao processar request:', e)