from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.API import getApiContent


async def inserirArquivoDIG(page: Page, id_interno: str) -> None:
    """
    Function that uploads the groups file of the Digital NewComers.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'Planilhas\\GRUPOS1.csv'
    
    print('Starting adjustments: "Inserir Arquivo DIG Grupos"')
    await page.goto(importgroup)
    print(f'Uploading {file_path}...')
    await page.set_input_files("#arg_file_groups_chooseLocalFile", files=file_path) # arquivo para o digital
    print('Unchecking...')
    await page.get_by_label("E-mail").uncheck()
    await page.get_by_label("Tarefas").uncheck()
    await page.get_by_label("Compartilhamento de arquivos").uncheck()
    await page.get_by_label("Blogs").uncheck()
    await page.get_by_label("Diários").uncheck()
    await page.get_by_label("Fórum de discussão").uncheck()
    await page.get_by_label("Wikis").uncheck()
    await page.get_by_label("Ferramentas do Mercado de").uncheck()
    print('Saving...')
    await page.get_by_role("button", name="Enviar").click()

async def inserirArquivoVET(page: Page, id_interno: str) -> None:
    """
    Function that uploads the groups file of the Digital Veterans.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"{baseURL}webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'Planilhas\\GRUPOS_SEM_FAEL.csv'

    print('Starting adjustments: "Inserir Arquivo Veteranos Grupos"')
    await page.goto(importgroup)
    print(f'Uploading {file_path}...')
    await page.set_input_files("#arg_file_groups_chooseLocalFile", files=file_path) #arquivo para o veteranos
    print('Unchecking...')
    await page.get_by_label("E-mail").uncheck()
    await page.get_by_label("Tarefas").uncheck()
    await page.get_by_label("Compartilhamento de arquivos").uncheck()
    await page.get_by_label("Blogs").uncheck()
    await page.get_by_label("Diários").uncheck()
    await page.get_by_label("Fórum de discussão").uncheck()
    await page.get_by_label("Wikis").uncheck()
    await page.get_by_label("Ferramentas do Mercado de").uncheck()
    print('Saving...')
    await page.get_by_role("button", name="Enviar").click()
    
async def atribuirGruposDIG(page: Page, id_interno: str) -> None:
    """
    Function that associates the groups to the discussion item
    'Desafio Colaborativo' Digital NewComers.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    print('Getting "Desafio Colaborativo" ID...')
    id_discussion = await getApiContent.API_Req_Content_Discussion(page=page, id_interno=id_interno, item_Search='Desafio Colaborativo')
    desafioURL = f'{classURL}/outline/discussion/{id_discussion}?view=discussions&courseId={id_interno}'

    print('Starting adjustments: "Atribuir Grupos Veteranos"')
    await page.goto(groups)
    print('Group visibility...')
    await page.get_by_role("gridcell", name="Desafio_Colaborativo | 7").get_by_role("button").click() #grupo para o digital
    await page.get_by_role("option", name="Visível para alunos").click()
    print('Opening "Desafion Colaborativo"...')
    await page.goto(desafioURL)
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('load')
    await page.wait_for_load_state('networkidle')
    print('Opening settings...')
    await page.evaluate('''document.querySelector("#discussion-settings-button").click()''')
    print('Associating group...')
    await page.get_by_role("link", name="Atribuir a grupos").click()
    await page.get_by_role("button", name="Personalizar").click()
    await page.get_by_role("option", name="Conjunto de grupos: Desafio").click()
    print('Saving...')
    await page.get_by_label("Salvar").click()
    await page.wait_for_load_state('networkidle')
    print('Saving...')
    await page.get_by_role("button", name="Salvar").click()
    await page.wait_for_load_state('networkidle')
    
    
async def atribuirGruposVET(page: Page, id_interno: str) -> None:
    """
    Function that associates the groups to the discussion item
    'Desafio Colaborativo' Digital Veterans.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    print('Getting "Desafio Colaborativo" ID...')
    id_discussion = await getApiContent.API_Req_Content_Discussion(page=page, id_interno=id_interno, item_Search='Desafio Colaborativo')
    desafioURL = f'{classURL}/outline/discussion/{id_discussion}?view=discussions&courseId={id_interno}'

    print('Starting adjustments: "Atribuir Grupos Veteranos"')
    await page.goto(groups)
    print('Group visibility...')
    await page.get_by_role("gridcell", name="Desafio_Colaborativo | 6").get_by_role("button").click() #grupo para o veteranos
    await page.get_by_role("option", name="Visível para alunos").click()
    print('Opening "Desafion Colaborativo"...')
    await page.goto(desafioURL)
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('load')
    await page.wait_for_load_state('networkidle')
    print('Opening settings...')
    await page.evaluate('''document.querySelector("#discussion-settings-button").click()''')
    print('Associating group...')
    await page.get_by_role("link", name="Atribuir a grupos").click()
    await page.get_by_role("button", name="Personalizar").click()
    await page.get_by_role("option", name="Conjunto de grupos: Desafio").click()
    print('Saving...')
    await page.get_by_label("Salvar").click()
    await page.wait_for_load_state('networkidle')
    print('Saving...')
    await page.get_by_role("button", name="Salvar").click()
    await page.wait_for_load_state('networkidle')