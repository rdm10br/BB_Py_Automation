from playwright.async_api import Playwright, async_playwright, expect, Page


async def API_Req_Content(page: Page, id_interno: str, item_Search: str) -> str:
    """
    Async Function to return if the id of the item was found, or not,
    This function find and return content ID with the API
    if it does not find then it returns the text
    'Erro na sala: ```id_interno``` no item: ```item_Search``` não foi
    encontrado'

    Args:
        page (Page): Page constructor form Playwright that
        you want this API to run
        id_interno (str): internal ID of the classroom you want to find
        that item
        item_Search (str): The name of the item you're searching

    Returns:
        str: Content_ID or if it doesn't find
        'Erro na sala: ```id_interno``` no item: ```item_Search``` não foi
        encontrado'
    """
    baseURL = "https://sereduc.blackboard.com/"
    
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents?title={item_Search}'
    
    print(f'Looking on Api Content for {item_Search} in {id_interno}')
    
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

async def API_Req_Content_children(page: Page, id_interno: str, father_id: str, item_Search: str) -> str:
    """
    Async Function to return if the id of the item was found, or not, but the
    item is a child node in the classroom
    This function find and return content ID with the API
    if it does not find then it returns the text
    'Erro na sala: ```id_interno``` no item: ```item_Search``` não foi
    encontrado'

    Args:
        page (Page): Page constructor form Playwright that
        you want this API to run
        id_interno (str): internal ID of the classroom you want to find
        that item
        item_Search (str): The name of the item you're searching

    Returns:
        str: Content_ID or if it doesn't find
        'Erro na sala: ```id_interno``` no item: ```item_Search``` não foi
        encontrado'
    """
    baseURL = "https://sereduc.blackboard.com/"
    
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children?title={item_Search}'
    
    print(f'Looking on Api Content Children for {item_Search} in {id_interno}')
    
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
            
async def API_Req_Content_Discussion(page: Page, id_interno: str, item_Search: str) -> str:
    """
    Async Function to return if the id of the item was found, or not,
    but the item_search is a Discussion type in the classroom
    This function find and return content ID with the API
    if it does not find then it returns the text
    'Erro na sala: ```id_interno``` no item: ```item_Search``` não foi
    encontrado'

    Args:
        page (Page): Page constructor form Playwright that
        you want this API to run
        id_interno (str): internal ID of the classroom you want to find
        that item
        item_Search (str): The name of the item you're searching

    Returns:
        str: TargetID or if it doesn't find
        'Erro na sala: ```id_interno``` no item: ```item_Search``` não foi
        encontrado'
    """
    baseURL = "https://sereduc.blackboard.com/"
    
    internalID_API = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents?title={item_Search}'

    print(f'Looking on Api Content Discussion for {item_Search} in {id_interno}')

    await page.goto(internalID_API)
    
    # request = '() => {return JSON.parse(document.body.innerText).results[0].id}'
    
    request = '''() => {
    const data = JSON.parse(document.body.innerText).results;
    if (data && data.length > 0 && data[0].contentHandler.targetId) {
        return data[0].contentHandler.targetId;
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