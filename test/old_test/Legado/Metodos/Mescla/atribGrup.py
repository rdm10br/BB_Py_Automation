from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *


def inserirArquivoDIG(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS1.csv'
    
    page.goto(importgroup)
    page.set_input_files("#arg_file_groups_chooseLocalFile", files=file_path) # arquivo para o digital
    page.get_by_label("E-mail").uncheck()
    page.get_by_label("Tarefas").uncheck()
    page.get_by_label("Compartilhamento de arquivos").uncheck()
    page.get_by_label("Blogs").uncheck()
    page.get_by_label("Diários").uncheck()
    page.get_by_label("Fórum de discussão").uncheck()
    page.get_by_label("Wikis").uncheck()
    page.get_by_label("Ferramentas do Mercado de").uncheck()
    page.get_by_role("button", name="Enviar").click()

def inserirArquivoVET(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS_SEM_FAEL.csv'
    
    page.goto(importgroup)
    page.set_input_files("#arg_file_groups_chooseLocalFile", files=file_path) #arquivo para o veteranos
    page.get_by_label("E-mail").uncheck()
    page.get_by_label("Tarefas").uncheck()
    page.get_by_label("Compartilhamento de arquivos").uncheck()
    page.get_by_label("Blogs").uncheck()
    page.get_by_label("Diários").uncheck()
    page.get_by_label("Fórum de discussão").uncheck()
    page.get_by_label("Wikis").uncheck()
    page.get_by_label("Ferramentas do Mercado de").uncheck()
    page.get_by_role("button", name="Enviar").click()
    
def atribuirGruposDIG(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    
    page.goto(groups)
    page.get_by_role("gridcell", name="Desafio Colaborativo | 7").get_by_role("button").click() #grupo para o digital
    page.get_by_role("option", name="Visível para alunos").click()
    page.get_by_role("link", name="Conteúdo da disciplina").click()
    page.get_by_role("link", name="Desafio Colaborativo").click()
    page.wait_for_load_state("networkidle")
    page.evaluate('''document.querySelector("#discussion-settings-button").click()''')
    page.get_by_role("link", name="Atribuir a grupos").click()
    page.get_by_role("button", name="Personalizar").click()
    page.get_by_role("option", name="Conjunto de grupos: Desafio").click()
    page.get_by_label("Salvar").click()
    page.get_by_role("button", name="Salvar").click()
    
def atribuirGruposVET(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    
    page.goto(groups)
    page.get_by_role("gridcell", name="Desafio Colaborativo | 6").get_by_role("button").click() #grupo para o veteranos
    page.get_by_role("option", name="Visível para alunos").click()
    page.get_by_role("link", name="Conteúdo da disciplina").click()
    page.get_by_role("link", name="Desafio Colaborativo").click()
    page.wait_for_load_state("networkidle")
    page.evaluate('''document.querySelector("#discussion-settings-button").click()''')
    page.get_by_role("link", name="Atribuir a grupos").click()
    page.get_by_role("button", name="Personalizar").click()
    page.get_by_role("option", name="Conjunto de grupos: Desafio").click()
    page.get_by_label("Salvar").click()
    page.get_by_role("button", name="Salvar").click()