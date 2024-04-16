from playwright.async_api import Playwright, async_playwright, expect, Page


async def inserirArquivoDIG(page: Page, id_interno) -> None:
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'Planilhas\\GRUPOS1.csv'
    
    await page.goto(importgroup)
    await page.set_input_files("#arg_file_groups_chooseLocalFile", files=file_path) # arquivo para o digital
    await page.get_by_label("E-mail").uncheck()
    await page.get_by_label("Tarefas").uncheck()
    await page.get_by_label("Compartilhamento de arquivos").uncheck()
    await page.get_by_label("Blogs").uncheck()
    await page.get_by_label("Diários").uncheck()
    await page.get_by_label("Fórum de discussão").uncheck()
    await page.get_by_label("Wikis").uncheck()
    await page.get_by_label("Ferramentas do Mercado de").uncheck()
    await page.get_by_role("button", name="Enviar").click()

async def inserirArquivoVET(page: Page, id_interno) -> None:
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'Planilhas\\GRUPOS_SEM_FAEL.csv'
    
    await page.goto(importgroup)
    await page.set_input_files("#arg_file_groups_chooseLocalFile", files=file_path) #arquivo para o veteranos
    await page.get_by_label("E-mail").uncheck()
    await page.get_by_label("Tarefas").uncheck()
    await page.get_by_label("Compartilhamento de arquivos").uncheck()
    await page.get_by_label("Blogs").uncheck()
    await page.get_by_label("Diários").uncheck()
    await page.get_by_label("Fórum de discussão").uncheck()
    await page.get_by_label("Wikis").uncheck()
    await page.get_by_label("Ferramentas do Mercado de").uncheck()
    await page.get_by_role("button", name="Enviar").click()
    
async def atribuirGruposDIG(page: Page, id_interno) -> None:
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    
    await page.goto(groups)
    await page.get_by_role("gridcell", name="Desafio Colaborativo | 7").get_by_role("button").click() #grupo para o digital
    await page.get_by_role("option", name="Visível para alunos").click()
    await page.get_by_role("link", name="Conteúdo da disciplina").click()
    await page.get_by_role("link", name="Desafio Colaborativo").click()
    await page.wait_for_load_state("networkidle")
    await page.evaluate('''document.querySelector("#discussion-settings-button").click()''')
    await page.get_by_role("link", name="Atribuir a grupos").click()
    await page.get_by_role("button", name="Personalizar").click()
    await page.get_by_role("option", name="Conjunto de grupos: Desafio").click()
    await page.get_by_label("Salvar").click()
    await page.get_by_role("button", name="Salvar").click()
    
async def atribuirGruposVET(page: Page, id_interno) -> None:
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    
    await page.goto(groups)
    await page.get_by_role("gridcell", name="Desafio_Colaborativo | 6").get_by_role("button").click() #grupo para o veteranos
    await page.get_by_role("option", name="Visível para alunos").click()
    await page.get_by_role("link", name="Conteúdo da disciplina").click()
    await page.get_by_role("link", name="Desafio Colaborativo").click()
    await page.wait_for_load_state("networkidle")
    await page.evaluate('''document.querySelector("#discussion-settings-button").click()''')
    await page.get_by_role("link", name="Atribuir a grupos").click()
    await page.get_by_role("button", name="Personalizar").click()
    await page.get_by_role("option", name="Conjunto de grupos: Desafio").click()
    await page.get_by_label("Salvar").click()
    await page.get_by_role("button", name="Salvar").click()