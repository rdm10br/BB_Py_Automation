import asyncio, pytest
from typing import Generator
from playwright.async_api import Playwright, async_playwright, expect, Page, APIRequestContext


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
    
    internalID_API = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents?title={item_Search}'''
    
    print(f'Looking on Api Content for {item_Search} in {id_interno}')
    
    await page.goto(internalID_API)
    
    #request = '()=> {return JSON.parse(document.body.innerText).results[0].id}'
    
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
            print(f'Erro na sala: {id_interno} no Item:'\
                  f'{item_Search} não foi encontrado')
            return
        else:
            print('Erro ao processar request:', e)


async def API_Req_Content_children(
    page: Page,
    id_interno: str,
    father_id: str,
    item_Search: str) -> str:
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
    
    internalID_API = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children?title={item_Search}'''
    
    print(f'Looking on Api Content Children for {item_Search} in {id_interno}')
    
    await page.goto(internalID_API)
    
    #request = '()=> {return JSON.parse(document.body.innerText).results[0].id}'
    
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
            print(f'Erro na sala: {id_interno} no Item: {item_Search} não foi'\
                  'encontrado')
            return
        else:
            print('Erro ao processar request:', e)
            
async def API_Req_Content_Discussion(
    page: Page,
    id_interno: str,
    item_Search: str) -> str:
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
    
    internalID_API = f'''{baseURL}learn/api/public/v1/courses/{id_interno}/contents?title={item_Search}'''

    print(f'Looking on Api Content Discussion for {item_Search} in'\
          f'{id_interno}')

    await page.goto(internalID_API)
    
    #request = '()=> {return JSON.parse(document.body.innerText).results[0].id}'
    
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
            print(f'Erro na sala: {id_interno} no Item:'\
                  f'{item_Search} não foi encontrado')
            return
        else:
            print('Erro ao processar request:', e)
         
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    headers = {
    }
    request_context = playwright.request.new_context(
        base_url="https://sereduc.blackboard.com/", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()
    

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        baseURL = "https://sereduc.blackboard.com/"
        await page.goto(baseURL)
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_timeout(10000)
        id_interno = '_187869_1'
        father_id = await API_Req_Content(page=page, id_interno=id_interno,
                    item_Search='Unidade 1')
        await page.wait_for_timeout(5000)
        folder_id = await API_Req_Content_children(page=page,
                    id_interno=id_interno, father_id=father_id,
                    item_Search='Atividade - Unidade 1')
        print(folder_id)
    return

if __name__ == "__main__":
    asyncio.run(main())