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
    
    await page.goto(api, wait_until='commit')
    try:
        await page.evaluate(request)
        is_ws = True
    except:
        is_ws = False
    
    # entra no black
    url_edit = f'./ultra/courses/{id_interno}/grades?gradebookView=grid'
    await page.goto(url=url_edit, wait_until='commit')
    await page.wait_for_load_state('domcontentloaded')
    print('Login na blackboard efetuado com sucesso')
    
    #entra no root
    url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
    await page.goto(url=url_edit, wait_until='commit')
    await page.wait_for_load_state('domcontentloaded')
    await page.get_by_role("button", name="Gerenciar").hover()
    await page.get_by_role("menuitem", name="Organização das colunas").click()
    print('Entrando no Root...')
        
    try:
        url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
        await page.goto(url=url_edit, wait_until='commit')
        await page.wait_for_load_state('domcontentloaded')
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        print('Ocultando os itens novamente...')
        # await page.get_by_label("AV1").first.check()
        if is_ws != True:
            await page.get_by_role("row", name="AV1 Não está em um Período de avaliação Nota calculada").get_by_label("AV1").check(timeout=2*1000)
            await page.wait_for_timeout(1000)
        await page.get_by_role("row", name="AV2 Não está em um Período de avaliação Nota calculada").get_by_label("AV2").check(timeout=2*1000)
        await page.wait_for_timeout(1000)
        await page.get_by_role("row", name="AF Não está em um Período de avaliação Nota calculada").get_by_label("AF").check(timeout=2*1000)
        await page.wait_for_timeout(1000)
        # await page.get_by_label("AV2").first.check()
        # await page.get_by_label("AF").first.check()

        await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
        await page.get_by_role("menuitem", name="Ocultar colunas selecionadas", exact=True).click()
        await page.get_by_role("button", name="Enviar").click()
        await page.wait_for_load_state("networkidle")
        await page.wait_for_load_state('load')
        print('Sala Ajustada com sucesso')
            
    except:
        if is_ws != True:
            try:
                await page.get_by_role("cell", name="AV1 (Oculto)").wait_for(state='visible', timeout=2000)
                print('AV1 Oculto')
            except:
                await page.get_by_role("row", name="AV1 Não está em um Período de avaliação Nota calculada").get_by_label("AV1").check(timeout=2*1000)
        try:
            await page.get_by_role("cell", name="AV2 (Oculto)").wait_for(state='visible', timeout=2000)
            print('AV2 Oculto')
        except:
            await page.get_by_role("row", name="AV2 Não está em um Período de avaliação Nota calculada").get_by_label("AV2").check(timeout=2*1000)
        try:
            await page.get_by_role("cell", name="AF (Oculto)").wait_for(state='visible', timeout=2000)
            print('AF Oculto')
        except:
            await page.get_by_role("row", name="AF Não está em um Período de avaliação Nota calculada").get_by_label("AF").check(timeout=2*1000)
        try:
            await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
            await page.get_by_role("menuitem", name="Ocultar colunas selecionadas", exact=True).click()
            await page.get_by_role("button", name="Enviar").click()
            await page.wait_for_load_state('load')
            print('Sala Ajustada com sucesso')
        except:
            print('Sala Ajustada com sucesso')