from playwright.sync_api import Playwright, sync_playwright, expect
from Metodos.API import getApiContent ,getPlanilha

def inserirArquivoEducI(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - Educação I 1.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoEducII(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - Educação II 1.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoEducIII(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - Educação III 1.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoExat(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - Exatas.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoNegI(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - NEGÓCIOS E GESTÃO I.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoNegII(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - NEGÓCIOS E GESTÃO II.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoNegIII(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - NEGÓCIOS E GESTÃO III.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoSaudI(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - SAÚDE I.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoSaudII(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - SAÚDE II.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoSaudIII(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - SAÚDE III.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoServ(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - SERVIÇO SOCIAL E TEOLOGIA.csv'
    
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
    page.wait_for_load_state('load')
    page.close()
    
def inserirArquivoInfo(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.new_page()
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'BB_Py_Automation\\Planilhas\\GRUPOS - TECNOLOGIA DA INFORMAÇÃO.csv'
    
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
    page.close()

def openFolderAV1(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    itemSearch = 'AV1 - Atividade Prática de Extensão'
    id_item = str(getApiContent.API_Req_Content(playwright,id_interno,itemSearch))
    folder = f'#folder-title-{id_item}'
    
    page.locator(folder).click()
    
def openFolderAV2(playwright: Playwright , id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    itemSearch = 'AV2 - Atividade Prática de Extensão'
    id_item = str(getApiContent.API_Req_Content(playwright,id_interno,itemSearch))
    folder = f'#folder-title-{id_item}'
    
    page.locator(folder).click()
    
def inserirGruposAtividadesAV1(playwright: Playwright ,curso):
    
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    classUrlUltra = page.url
    item = f'Envio AV1 - Atividade Prática de Extensão ({curso})'
    searchURL = f'{classUrlUltra}?search={item}'
    
    page.goto(searchURL)
    page.get_by_role("button", name="Condições de liberação").click()
    page.get_by_role("option", name="Condições de liberação").click()
    page.get_by_label("Condições de liberação de").click()
    page.get_by_label("Membros ou grupos específicos").check()
    page.get_by_label("Membros ou grupos específicos").fill(curso)
    page.get_by_role("button", name="Salvar").click()
    page.wait_for_load_state('load')

def inserirGruposAtividadesAV2(playwright: Playwright ,curso):
    
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    classUrlUltra = page.url()
    item = f'Envio AV2 - Atividade Prática de Extensão ({curso})'
    searchURL = f'{classUrlUltra}?search={item}'
    
    page.goto(searchURL)
    page.get_by_role("button", name="Condições de liberação").click()
    page.get_by_role("option", name="Condições de liberação").click()
    page.get_by_label("Condições de liberação de").click()
    page.get_by_label("Membros ou grupos específicos").check()
    page.get_by_label("Membros ou grupos específicos").fill(curso)
    page.get_by_role("button", name="Salvar").click()
    page.wait_for_load_state('load')