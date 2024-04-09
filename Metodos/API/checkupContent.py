from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.API import getApiContent

async def checkup_Req(page: Page, id_interno ,item_Search) -> None:
    
    result = getApiContent.API_Req_Content(page=page, id_interno=id_interno, item_Search=item_Search)
    
    if result is f'Erro na sala: {id_interno} no Item: {item_Search} não foi encontrado' :
        return