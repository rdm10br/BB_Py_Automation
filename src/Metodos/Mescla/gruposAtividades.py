from playwright.async_api import Page
from Metodos.API import getApiContent
from unidecode import unidecode
import regex as re


async def inserirArquivo(page: Page, id_interno: str, Area: str) -> None:
    """
    Function that uploads the groups file according to the ```Area```.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
        Area (str): Course Area of the classroom
    """
    # baseURL = "https://sereduc.blackboard.com/"
    importgroup = f"./webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id="\
        f"{id_interno}&toggleType=all&fromPage=groups"
    Area = re.sub(r"\[\'", '', Area)
    Area = re.sub(r"\'\]", '', Area)
    file_path = fr'Planilhas\Grupo - {Area}.csv'

        
    print(f'Uploading group: {file_path}')
    await page.goto(importgroup)
    await page.set_input_files("#arg_file_groups_chooseLocalFile", files=file_path)
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
    await page.wait_for_load_state('load')


async def ID_FolderAV1(page: Page, id_interno) -> None:
    itemSearch = 'AV1 - Atividade Prática de Extensão'
    id_item = str(getApiContent.API_Req_Content(page=page,
                                                id_interno=id_interno, item_Search=itemSearch))
    return id_item


async def ID_FolderAV2(page: Page, id_interno) -> None:
    itemSearch = 'AV2 - Atividade Prática de Extensão'
    id_item = str(getApiContent.API_Req_Content(page=page,
                                                id_interno=id_interno, item_Search=itemSearch))
    return id_item


async def inserirGruposAtividadesAV1(page: Page, id_interno, curso):
    # baseURL = 'https://sereduc.blackboard.com/'
    classUrlUltra = f'./ultra/courses/{id_interno}/outline'
    item = f'Envio AV1 - Atividade Prática de Extensão ({curso})'
    searchURL = f'{classUrlUltra}?search={item}'
    # folder_id = ID_FolderAV1(playwright , id_interno)
    # content_ID = getApiContent.API_Req_Content_children(page=page, id_interno=id_interno, father_id=folder_id, item_Search=item)
    # URLConditional = f'{classUrlUltra}/conditionalRelease?contentId={content_ID}'

    print(f'Opening {item}...')
    await page.goto(searchURL)
    print('Opening config...')
    await page.get_by_label("Condições de liberação de").click()
    print('Checking...')
    await page.get_by_label("Membros ou grupos específicos").check()
    print('Opening comboBox...')
    await page.locator("#course-groups-combobox").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(1500)
    cursos = unidecode(curso)
    print(f'Associating group: {cursos} to {item}')
    await page.locator("#course-groups-combobox-search-box").fill(value=curso)
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(1500)
    await page.locator("#course-groups-combobox-menu > li > ul", has_text=curso).click()
    await page.wait_for_timeout(1500)
    print('Clicking out...')
    await page.get_by_text('Você pode limitar o acesso a este conteúdo. Escolha').click()
    print('Saving...')
    await page.get_by_role("button", name="Salvar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(1500)
    await page.goto(classUrlUltra)


async def inserirGruposAtividadesAV2(page: Page, id_interno, curso):
    # baseURL = 'https://sereduc.blackboard.com/'
    classUrlUltra = f'./ultra/courses/{id_interno}/outline'
    item = f'Envio AV2 - Atividade Prática de Extensão ({curso})'
    searchURL = f'{classUrlUltra}?search={item}'
    # folder_id = ID_FolderAV1(playwright , id_interno)
    # content_ID = getApiContent.API_Req_Content_children(playwright=playwright, id_interno=id_interno, folder_id=folder_id, item_Search=item)
    # URLConditional = f'{classUrlUltra}/conditionalRelease?contentId={content_ID}'

    print(f'Opening {item}...')
    await page.goto(searchURL)
    # await page.get_by_role("button", name="Condições de liberação").click()
    # await page.get_by_role("option", name="Condições de liberação").click()

    print('Opening config...')
    await page.get_by_label("Condições de liberação de").click()
    print('Checking...')
    await page.get_by_label("Membros ou grupos específicos").check()
    print('Opening comboBox...')
    await page.locator("#course-groups-combobox").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(1500)
    cursos = unidecode(curso)
    print(f'Associating group: {cursos} to {item}')
    await page.locator("#course-groups-combobox-search-box").fill(value=curso)
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(1500)
    await page.locator("#course-groups-combobox-menu > li > ul", has_text=curso).click()
    await page.wait_for_timeout(1500)
    print('Clicking out...')
    await page.get_by_text('Você pode limitar o acesso a este conteúdo. Escolha').click()
    print('Saving...')
    await page.get_by_role("button", name="Salvar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(1500)
    await page.goto(classUrlUltra)