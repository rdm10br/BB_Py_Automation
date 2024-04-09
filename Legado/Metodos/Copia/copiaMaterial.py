from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
from Metodos.API import getPlanilha

def copyMaterial(playwright: Playwright , index) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    id_master = getPlanilha.getCell_plan2(index=index)
    id_copia = getPlanilha.getCell_copy_plan2(index=index)
    baseURL = "https://sereduc.blackboard.com/"
    coppyOnBlack = f"{baseURL}webapps/blackboard/execute/copy_content?navItem=copy_course_content_new&target=no&type=course"
    
    page.goto(coppyOnBlack)
    
    page.get_by_label("Selecionar Tipo de cópia").select_option("O") #curso existente
    # page.get_by_label("Selecionar Tipo de cópia").select_option("N") #nova disciplina
    # page.get_by_label("Selecionar Tipo de cópia").select_option("E") #copia exata
    
    page.get_by_label("Código do Curso de Origem").fill(value=id_master)
    page.get_by_label("Código do Curso de Destino").fill(value=id_copia)
    page.locator('#bottom_Submit').click()
    page.wait_for_load_state('domcontentloaded')
    page.evaluate('document.querySelector("#stepcontent2 > ol > li:nth-child(4) > div > div > a:nth-child(1)").click()')
    # page.get_by_label('Imagem de banner').uncheck()
    page.locator('#bottom_Submit').click()
    
# with sync_playwright() as playwright:
    # copyMaterial(playwright ,index=1)