from playwright.sync_api import Playwright, sync_playwright, expect
from Metodos.API import getApiContent

def ajusteAvaliacao(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    itemSearch = 'Avaliações'
    id_avaliacao = str(getApiContent.API_Req_Content(playwright=playwright, id_interno=id_interno, item_Search=itemSearch))
    
    page.wait_for_load_state('domcontentloaded')
    page.press('body','End')
    page.wait_for_load_state('domcontentloaded')
    page.press('body','End')
    page.locator(f'#folder-title-{id_avaliacao}').click()
    page.get_by_label("Mais opções para Regras da").click()
    page.get_by_text("Editar", exact=True).click()
    page.get_by_role("heading", name="Regras da Avaliação - Resolu").click()
    page.get_by_label("Novo link de LTI em undefined").click(click_count=3)
    page.get_by_label("Novo link de LTI em undefined").fill("Regras da Avaliação - Resolução CONSU")
    page.get_by_label("Novo link de LTI em undefined").press("Enter")
    page.wait_for_load_state('domcontentloaded')
    page.get_by_role("button", name="Salvar").click()
    

# with sync_playwright() as playwright:
#     idInterno = '_139625_1'
#     ajusteAvaliacao(playwright,idInterno)