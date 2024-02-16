from playwright.sync_api import Playwright, sync_playwright, expect
import getApiContent

def ajusteSofia(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    itemSearch = 'Sofia'
    id_sofia = getApiContent.API_Req_Content(playwright,id_interno,itemSearch)
    page.wait_for_load_state('domcontentloaded')
    
    url = page.url
    
    
    page.goto(url+"/edit/lti/"+id_sofia)
    # page.wait_for_load_state('domcontentloaded')
    page.get_by_placeholder("Formato: meuwebsite.com").click(click_count=3)
    page.get_by_placeholder("Formato: meuwebsite.com").fill("sofialti.ldmedtech.com.br/v1/launch/ser-sofia-plano-estudos")
    # page.wait_for_load_state('domcontentloaded')
    page.wait_for_load_state('networkidle')
    page.get_by_role("button", name="Salvar").click()
    page.wait_for_load_state('networkidle')
    # page.wait_for_load_state('domcontentloaded')
    page.get_by_text("Você precisará desta informa").click()
    page.goto(url)
    # page.wait_for_load_state('domcontentloaded')