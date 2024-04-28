from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.API import getApiContent

async def checkup_Req(page: Page, id_interno: str ,item_Search: str) -> str:
    """
    Async Function to return if the id of the item was found, or not,
    This function calls the function to find and return content ID with the API
    if it does not find then it returns the text 
    'Erro na sala: ```id_interno``` no item: ```item_Search``` não foi 
    encontrado'
    
    Args:
        page (Page): Page constructor form Playwright that 
        you want this API to run
        id_interno (str): internal ID of the classroom you want to find
        that item
        item_Search (str): The name of the item you're searching
    """    
    result = getApiContent.API_Req_Content(page=page, id_interno=id_interno, item_Search=item_Search)
    
    if result is f'Erro na sala: {id_interno} no Item: {item_Search} não foi encontrado' :
        return result
    
    return result