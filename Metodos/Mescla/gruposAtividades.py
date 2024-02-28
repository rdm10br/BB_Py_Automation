from playwright.sync_api import Playwright, sync_playwright, expect
from Metodos.API import getApiContent ,getPlanilha

def inserirArquivoAV1(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS1.csv'
    
    page.goto(importgroup)
    page.set_input_files("#arg_file_groups_chooseLocalFile",file_path) # arquivo para o digital
    page.get_by_label("E-mail").uncheck()
    page.get_by_label("Tarefas").uncheck()
    page.get_by_label("Compartilhamento de arquivos").uncheck()
    page.get_by_label("Blogs").uncheck()
    page.get_by_label("Diários").uncheck()
    page.get_by_label("Fórum de discussão").uncheck()
    page.get_by_label("Wikis").uncheck()
    page.get_by_label("Ferramentas do Mercado de").uncheck()
    page.get_by_role("button", name="Enviar").click()
    
def inserirArquivoAV2(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS1.csv'
    
    page.goto(importgroup)
    page.set_input_files("#arg_file_groups_chooseLocalFile",file_path) # arquivo para o digital
    page.get_by_label("E-mail").uncheck()
    page.get_by_label("Tarefas").uncheck()
    page.get_by_label("Compartilhamento de arquivos").uncheck()
    page.get_by_label("Blogs").uncheck()
    page.get_by_label("Diários").uncheck()
    page.get_by_label("Fórum de discussão").uncheck()
    page.get_by_label("Wikis").uncheck()
    page.get_by_label("Ferramentas do Mercado de").uncheck()
    page.get_by_role("button", name="Enviar").click()

def atribuirGruposAV1(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    # groups = f'{classURL}/groups'
    
    itemSearch = 'AV1 - Atividade Prática de Extensão'
    id_item = str(getApiContent.API_Req_Content(playwright,id_interno,itemSearch))
    folder = f'#folder-title-{id_item}'
    curso = getPlanilha.getCell()
    item_name = f'Envio AV1 - Atividade Prática de Extensão ({curso})'
    
    # page.goto(groups)
    # page.get_by_role("gridcell", name="Desafio Colaborativo").get_by_role("button").click()
    
    page.locator(folder).click()
    page.get_by_role("link", name=item_name, exact=True).click()
    page.get_by_role("button", name="Condições de liberação").click()
    page.get_by_role("menuitem", name="Condições de liberação").click()
    page.get_by_label("Membros ou grupos específicos").check()
    page.get_by_label("Membros ou grupos específicos").fill(curso)
    page.get_by_role("button", name="Salvar").click()
    
def atribuirGruposAV2(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    
    itemSearch = 'AV2 - Atividade Prática de Extensão'
    id_item = str(getApiContent.API_Req_Content(playwright,id_interno,itemSearch))
    folder = f'#folder-title-{id_item}'
    curso = getPlanilha.getCell()
    item_name = f'Envio AV2 - Atividade Prática de Extensão ({curso})'
    
    # page.goto(groups)
    # page.get_by_role("gridcell", name="Desafio Colaborativo").get_by_role("button").click()
    
    page.locator(folder).click()
    page.get_by_role("link", name=item_name, exact=True).click()
    page.get_by_role("button", name="Condições de liberação").click()
    page.get_by_role("menuitem", name="Condições de liberação").click()
    page.get_by_label("Membros ou grupos específicos").check()
    page.get_by_label("Membros ou grupos específicos").fill(curso)
    page.get_by_role("button", name="Salvar").click()