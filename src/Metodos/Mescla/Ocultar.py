from playwright.sync_api import Page


async def ocultar_boletim(page: Page, id_interno: str) -> None:
    
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'
    request = '''() => {
    const data = JSON.parse(document.body.innerText).results;
    if (data && data.length > 0 && data.find(item => item.columnName == "Avaliação Workshop")) {
        return data.find(item => item.columnName == "Avaliação Workshop");
    } else {
        throw new Error('Item não encontrado');
    }
    }'''
    # config = 'JSON.parse(document.body.innerText).results.find(item => item.columnName == "Avaliação Workshop")'
    
    async def loop_AV1(page: Page) -> bool:
        await page.get_by_role("cell", name="AV1 (Oculto)").wait_for(state='visible', timeout=2000)
        await page.wait_for_timeout(6*1000)
        print('AV1 Desocultando...')
        await page.get_by_label("AV1").check(timeout=6*1000)
        await page.wait_for_timeout(6*1000)
        await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
        await page.get_by_role("menuitem", name="Mostrar colunas selecionadas", exact=True).click()
        await page.wait_for_timeout(6*2000)
        await page.get_by_role("button", name="Enviar").click()
        await page.wait_for_load_state("networkidle")
        await page.wait_for_load_state('load')
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        await page.get_by_role("row", name="AV1 Não está em um Período de avaliação Nota calculada").get_by_label("AV1").wait_for(state='visible', timeout=6*1000)
        await page.wait_for_timeout(6*1000)
        print('AV1 desocultada!')
        return False
    
    await page.goto(api, wait_until='commit')
    try:
        await page.evaluate(request)
        is_ws = True
    except:
        is_ws = False
        
    checkAV1: bool = True
        
    try:
        url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
        await page.goto(url=url_edit, wait_until='commit')
        await page.wait_for_load_state('domcontentloaded')
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        print('Ocultando os itens novamente...')
        if is_ws != True:
            await page.get_by_role("row", name="AV1 Não está em um Período de avaliação Nota calculada").get_by_label("AV1").check(timeout=6*1000)
            await page.wait_for_timeout(6*2000)
        await page.get_by_role("row", name="AV2 Não está em um Período de avaliação Nota calculada").get_by_label("AV2").check(timeout=6*1000)
        await page.wait_for_timeout(6*2000)
        await page.get_by_role("row", name="AF Não está em um Período de avaliação Nota calculada").get_by_label("AF").check(timeout=6*1000)
        await page.wait_for_timeout(6*2000)

        await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
        await page.get_by_role("menuitem", name="Ocultar colunas selecionadas", exact=True).click()
        await page.wait_for_timeout(6*2000)
        await page.get_by_role("button", name="Enviar").click()
        await page.wait_for_load_state("networkidle")
        await page.wait_for_load_state('load')
        print('Sala Ajustada com sucesso')
            
    except:
        if is_ws != True:
            try:
                await page.get_by_role("cell", name="AV1 (Oculto)").wait_for(state='visible', timeout=2000)
                await page.wait_for_timeout(6*1000)
                print('AV1 Oculto')
            except:
                try:
                    await page.get_by_role("row", name="AV1 Não está em um Período de avaliação Nota calculada").get_by_label("AV1").check(timeout=6*1000)
                    await page.wait_for_timeout(6*1000)
                except:
                    print('AV1 calculada não existe')
        else:
            while checkAV1:
                try:
                    checkAV1 = await loop_AV1(page)
                except Exception as e:
                    if await page.get_by_role("row", name="AV1 Não está em um Período de avaliação Nota calculada").get_by_label("AV1").is_visible(timeout = 1*2000):
                        checkAV1 = False
                    else:
                        print(f'error: {e}')
        try:
            await page.get_by_role("cell", name="AV2 (Oculto)").wait_for(state='visible', timeout=2000)
            await page.wait_for_timeout(6*1000)
            print('AV2 Oculto')
        except:
            try:
                await page.get_by_role("row", name="AV2 Não está em um Período de avaliação Nota calculada").get_by_label("AV2").check(timeout=6*1000)
                await page.wait_for_timeout(6*1000)
            except:
                print('AV2 calculada não existe')
        try:
            await page.get_by_role("cell", name="AF (Oculto)").wait_for(state='visible', timeout=2000)
            await page.wait_for_timeout(6*1000)
            print('AF Oculto')
        except:
            try:
                await page.get_by_role("row", name="AF Não está em um Período de avaliação Nota calculada").get_by_label("AF").check(timeout=6*1000)
                await page.wait_for_timeout(6*1000)
            except:
                print('AF calculada não existe')
        try:
            await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
            await page.get_by_role("menuitem", name="Ocultar colunas selecionadas", exact=True).click()
            await page.wait_for_timeout(6*2000)
            await page.get_by_role("button", name="Enviar").click()
            await page.wait_for_load_state("networkidle")
            await page.wait_for_load_state('load')
            print('Sala Ajustada com sucesso')
        except:
            print('Sala Ajustada com sucesso')
            

async def AdeusCTRL2(
    page: Page,
    id_interno: str,
    Item_list: list = [
        'Atividade de Autoaprendizagem 1',
        'Atividade de Autoaprendizagem 2',
        'Atividade de Autoaprendizagem 3',
        'Atividade de Autoaprendizagem 4',
        'Avaliação Workshop',
        'Atividade Contextualizada',
        'AV1*',
        'AV2*',
        'AF*'
        ]) -> None:
    
    """_summary_

    Args:
        page (Page): _description_
        id_interno (str): _description_
        Item_list (list, optional): _description_. Defaults to [ 'Atividade de Autoaprendizagem 1', 'Atividade de Autoaprendizagem 6', 'Atividade de Autoaprendizagem 3', 'Atividade de Autoaprendizagem 6', 'Avaliação Workshop', 'Atividade Contextualizada', 'AV1*', 'AV2*', 'AF*' ].

    Returns:
        _type_: _description_
    """
     
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'
    def request(item: str):return f'JSON.parse(document.body.innerText).results.find(item => item.columnName == "{item}" && item.visibleInBook == true).position'
    await page.goto(api, wait_until='networkidle')
    position = []
    position_dict: dict = {}
    
    for i in Item_list:
        try:
            position.append(await page.evaluate(request(i)))
            position_dict[await page.evaluate(request(i))] = i
            print(f'item: {i} foi encontrado e não está oculto')
        except:
            print(f'item: {i} não encontrado ou já está oculto')
    if len(position) > 0:
        try:
            url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
            await page.goto(url=url_edit, wait_until='commit')
            await page.wait_for_load_state('domcontentloaded')
                
            # for p in position:
            #     try:
            #         await page.locator(f"#cmlink_h{p}").click(timeout=6*1000)
            #         await page.get_by_role("link", name="Ocultar dos alunos (ligado/").click()
            #         await page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("columnheader", name="Coluna não visível para usuáriosNota Geral Clique para obter mais opções").locator("span").click()
            #         await page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("link", name="Ocultar dos alunos (ligado/").click()
            #         await page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("columnheader", name="Nota Geral Clique para obter mais opções", exact=True).locator("span").click()
            #     except:
            #         ...
            
            await page.get_by_role("button", name="Gerenciar").hover()
            await page.get_by_role("menuitem", name="Organização das colunas").click()
            print('Ocultando os itens novamente...')
            
            for p in position:
                await page.locator(f"[id=\"item_{p}\\.layoutCheckBox\"]").wait_for(state='visible', timeout=6*1000)
                await page.locator(f"[id=\"item_{p}\\.layoutCheckBox\"]").check()
            await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
            await page.get_by_role("menuitem", name="Ocultar colunas selecionadas", exact=True).click()
            await page.wait_for_timeout(6*2000)
            await page.get_by_role("button", name="Enviar").click()
            await page.wait_for_load_state("networkidle")
            await page.wait_for_load_state('load')
            print('Sala Ajustada com sucesso')
        except:
            print('Sala Ajustada com sucesso')
    else:
        print('Todas as calculadas estão ocultas')