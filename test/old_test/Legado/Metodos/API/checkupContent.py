from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *

from Metodos.API import getApiContent

def checkup_Req(playwright: Playwright  ,id_interno ,item_Search) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    
    result = getApiContent.API_Req_Content(playwright=playwright, id_interno=id_interno, item_Search=item_Search)
    
    if result is f'Erro na sala: {id_interno} no Item: {item_Search} não foi encontrado' :
        return