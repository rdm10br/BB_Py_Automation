from playwright.async_api import Page


from Metodos.API import getApiContent

    
async def inserirArquivo(page: Page, id_interno: str) -> None:
    """
    Function that uploads the groups file of the Digital NewComers.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    importgroup = f"./webapps/bb-group-mgmt-LEARN/jsp/groupspace/ex/ImportGroups.jsp?course_id={id_interno}&toggleType=all&fromPage=groups"
    file_path = 'Planilhas\\GRUPOS - FAEL - VET.csv'
    
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

    
async def atribuirGruposFael(page: Page, id_interno: str) -> None:
    """
    Function that associates the groups to the discussion item
    'Converse com a sua Turma'.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    classURL = f'./ultra/courses/{id_interno}'
    groups = f'{classURL}/groups'
    item_search = 'Converse com a sua Turma'
    print('Getting "Converse com a sua Turma" ID...')
    try:
        id_discussion = await getApiContent.API_Req_Content_Discussion(page=page, id_interno=id_interno, item_Search=item_search)
    except Exception as e:
        if 'Item não encontrado' in str(e):
            print(f'Erro na sala: {id_interno}; Item: {item_search} não foi encontrado')
            pass
        else:
            print('Erro ao processar request:', e)
            pass
    if id_discussion != None:
        desafioConfigURL = f'{classURL}/outline/discussion/{id_discussion}/settings?contentId={id_discussion}&view=discussions&courseId={id_interno}'
        await page.goto(groups)
        print('Group visibility...')
        await page.get_by_role("gridcell", name="Coligada | 1").get_by_role("button").click()
        await page.get_by_role("option", name="Visível para alunos").click()
        print('Opening item...')
        await page.goto(url=desafioConfigURL, wait_until='commit')
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_load_state('load')
        await page.wait_for_load_state('networkidle')
        print('Opening settings...')
        print('Associating group...')
        if await page.get_by_role("link", name="Nenhum grupo").is_visible() is True:
            await page.get_by_role("button", name="Excluir grupo").click(timeout=4*1000)
            await page.get_by_role("button", name="Excluir").click()
            await page.get_by_role("link", name="Atribuir a grupos").click()
            await page.get_by_role("button", name="Personalizar").click()
            await page.get_by_role("option", name="Conjunto de grupos: Coligada").click()
            print('Saving...')
            await page.get_by_label("Salvar").click()
            await page.wait_for_load_state('networkidle')
            print('Saving...')
            await page.get_by_role("button", name="Salvar").click()
            await page.wait_for_load_state('networkidle')
            pass
        else:
            await page.get_by_role("link", name="Atribuir a grupos").wait_for(state='visible', timeout=4*1000)
            await page.get_by_role("link", name="Atribuir a grupos").click(timeout=4*1000)
            await page.get_by_role("button", name="Personalizar").click()
            await page.get_by_role("option", name="Conjunto de grupos: Coligada").click()
            print('Saving...')
            try:
                print('teste - nenhum grupo')
                await page.get_by_text("Nenhum grupo encontrado").wait_for(state='visible', timeout=5*1000)
                print('pass...')
                if await page.get_by_text("Nenhum grupo encontrado").is_visible() is True:
                    print(f'Error de Modal na sala {id_interno} no item {item_search}')
                    loc = "body > div.MuiDialogroot-0-2-2 > div.MuiDialogcontainer-0-2-5.makeStylescontainer-0-2-1.MuiDialogscrollBody-0-2-4 > div > div > div.MuiDialogActionsroot-0-2-1402.MuiDialogActionsspacing-0-2-1403 > button > span"
                    loc = "body > div.MuiDialogroot-0-2-2 > div.MuiDialogcontainer-0-2-5.makeStylescontainer-0-2-1.MuiDialogscrollBody-0-2-4 > div > div > div.MuiDialogActionsroot-0-2-1405.MuiDialogActionsspacing-0-2-1406 > button"
                    await page.locator("button > span", has_text='OK').click(timeout=1.8*1_000_000)
                await page.get_by_label("Salvar").click()
                await page.wait_for_load_state('networkidle')
                print('Saving...')
                await page.get_by_role("button", name="Salvar").click()
                await page.wait_for_load_state('networkidle')
            except:
                await page.get_by_label("Salvar").click()
                await page.wait_for_load_state('networkidle')
                print('Saving...')
                await page.get_by_role("button", name="Salvar").click()
                await page.wait_for_load_state('networkidle')
        #check if modal error
        if await page.get_by_text("Olá! Para acessar este recurso você precisa estar matriculado na sala").is_visible() is True:
            print(f'Error de Modal na sala {id_interno} no item {item_search}')
            await page.locator('#notification-modal-api-error > div.reveal-modal__header > button').click()
            pass
        else:
            pass
    else:
        print(f'Item: {item_search} não encontrado!')
        pass