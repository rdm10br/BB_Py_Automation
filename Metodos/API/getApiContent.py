from playwright.async_api import Playwright, async_playwright, expect, Page


async def API_Req_Content(page: Page, id_interno, item_Search) -> None:
    
    baseURL = "https://sereduc.blackboard.com/"
    
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents?title={item_Search}'
    
    await page.goto(internalID_API)
    
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
        id_sofia = await page.evaluate(request)
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

async def API_Req_Content_children(page: Page, id_interno, father_id, item_Search) -> None:
    
    baseURL = "https://sereduc.blackboard.com/"
    
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children?title={item_Search}'
    
    await page.goto(internalID_API)
    
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
        id_sofia = await page.evaluate(request)
        # print(str(id_sofia))
        return str(id_sofia)
    except Exception as e:
        if 'Item não encontrado' in str(e):
            print(f'Erro na sala: {id_interno} no Item: {item_Search} não foi encontrado')
            return
        else:
            print('Erro ao processar request:', e)